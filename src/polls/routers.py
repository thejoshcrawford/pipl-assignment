from rest_framework import routers
from polls_api.viewsets import PollViewSet, PollResponseViewSet

router = routers.DefaultRouter()

router.register(r'poll', PollViewSet)
router.register(r'pollresponse', PollResponseViewSet)
