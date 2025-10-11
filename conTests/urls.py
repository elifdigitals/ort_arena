from rest_framework.routers import DefaultRouter
from .views import (
    ContestViewSet,
    ContestExerciseViewSet,
    ContestParticipantViewSet,
    ParticipantAnswerViewSet
)

router = DefaultRouter()
router.register('contests', ContestViewSet)
router.register('contest-exercises', ContestExerciseViewSet)
router.register('participants', ContestParticipantViewSet)
router.register('answers', ParticipantAnswerViewSet)

urlpatterns = router.urls
