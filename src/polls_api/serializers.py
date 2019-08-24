from rest_framework import serializers
from .models import Poll, PollOption, PollResponse     

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PollResponseSerializer(serializers.ModelSerializer):
    ip = serializers.CharField(required=False)
    user_agent = serializers.CharField(required=False)

    class Meta:
        model = PollResponse
        fields = ['poll_option', 'ip', 'user_agent']

    def create(self, validated_data):
        request = self.context.get("request")
        ip = get_client_ip(request)
        user_agent = request.META['HTTP_USER_AGENT']

        # check for existing vote
        poll_option_id = validated_data.get('poll_option').pk
        poll_option = PollOption.objects.get(id=poll_option_id)
        poll_id = poll_option.poll.pk
        if PollResponse.objects.filter(poll_option__poll__id=poll_id,ip=ip,user_agent=user_agent).exists():
            raise serializers.ValidationError("You may not vote twice on a poll.")
        
        validated_data['ip'] = ip
        validated_data['user_agent'] = user_agent
        return PollResponse.objects.create(**validated_data)

class PollOptionSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = PollOption
        fields = '__all__'

    def get_count(self, obj):
        return obj.response.count()

class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True, read_only=True)
    voted = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Poll
        fields = '__all__'

    def get_voted(self, obj):
        request = self.context.get("request")
        ip = get_client_ip(request)
        user_agent = request.META['HTTP_USER_AGENT']
        poll_id = obj.pk

        if PollResponse.objects.filter(poll_option__poll__id=poll_id,ip=ip,user_agent=user_agent).exists():
            return True
        return False