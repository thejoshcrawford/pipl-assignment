from rest_framework import viewsets, mixins
from .models import Poll, PollResponse
from .serializers import PollSerializer, PollResponseSerializer

class PollViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollResponseViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = PollResponse.objects.all()
    serializer_class = PollResponseSerializer