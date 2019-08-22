from rest_framework import serializers
from .models import Poll, PollOption, PollResponse        

class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = ['title']

class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = '__all__'

    def create(self, validated_data):
        options = validated_data.pop('options')

        new_poll = Poll.objects.create(**validated_data)
        
        for option in options:
            PollOption.objects.create(poll=new_poll, **option)

        print(new_poll)
        print(new_poll.title)
        # print(poll.options)

        return new_poll


class PollResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollResponse
        fields = '__all__'

