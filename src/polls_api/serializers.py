from rest_framework import serializers
from .models import Poll, PollOption, PollResponse        

class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class PollResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollResponse
        fields = '__all__'

