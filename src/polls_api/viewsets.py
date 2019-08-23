from rest_framework import viewsets, mixins
from .models import Poll, PollOption, PollResponse
from .serializers import PollSerializer, PollOptionSerializer, PollResponseSerializer

class PollViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    lookup_field = 'url'

class PollOptionViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = PollOption.objects.all()
    serializer_class = PollOptionSerializer

class PollResponseViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = PollResponse.objects.all()
    serializer_class = PollResponseSerializer