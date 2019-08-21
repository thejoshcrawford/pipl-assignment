from rest_framework import routers
from polls_api.viewsets import PollViewSet

router = routers.DefaultRouter()

router.register(r'poll', PollViewSet)
