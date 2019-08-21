from rest_framework import serializers
from .models import Poll, PollResponse        

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class PollResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollResponse
        fields = '__all__'