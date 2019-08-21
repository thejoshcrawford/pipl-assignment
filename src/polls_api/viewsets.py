from rest_framework import viewsets, mixins
from .models import Poll
from .serializers import PollSerializer

class PollViewSet(
    mixins.CreateModelMixin, 
    mixins.RetrieveModelMixin, 
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer