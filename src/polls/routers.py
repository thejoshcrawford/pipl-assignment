from rest_framework import routers
from polls_api.viewsets import PollViewSet, PollOptionViewSet, PollResponseViewSet

router = routers.DefaultRouter()

router.register(r'poll', PollViewSet)
router.register(r'poll_option', PollOptionViewSet)
router.register(r'poll_response', PollResponseViewSet)
