from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    ContestViewSet,
    ContestExerciseViewSet,
    ContestParticipantViewSet,
    ParticipantAnswerViewSet,
    CreateDuelView, 
    AcceptDuelView, 
    RejectDuelView, 
    FinishDuelView
)

router = DefaultRouter()
router.register('contests', ContestViewSet)
router.register('contest-exercises', ContestExerciseViewSet)
router.register('participants', ContestParticipantViewSet)
router.register('answers', ParticipantAnswerViewSet)

urlpatterns = [
    path('duel/create/', CreateDuelView.as_view(), name='create_duel'),
    path('duel/<int:pk>/accept/', AcceptDuelView.as_view(), name='accept_duel'),
    path('duel/<int:pk>/reject/', RejectDuelView.as_view(), name='reject_duel'),
    path('duel/<int:pk>/finish/', FinishDuelView.as_view(), name='finish_duel'),
]

urlpatterns = router.urls
