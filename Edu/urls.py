from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, TopicViewSet, ExerciseViewSet, ExerciseTestViewSet

router = DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('topics', TopicViewSet)
router.register('exercises', ExerciseViewSet)
router.register('exercise-tests', ExerciseTestViewSet)

urlpatterns = router.urls
