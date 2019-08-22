from rest_framework import routers
from polls_api.viewsets import PollViewSet, PollOptionViewSet, PollResponseViewSet

router = routers.DefaultRouter()

router.register(r'poll', PollViewSet)
router.register(r'polloption', PollOptionViewSet)
router.register(r'pollresponse', PollResponseViewSet)
