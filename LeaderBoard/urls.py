from django.urls import path
from . import views

urlpatterns = [
    path('subject/<int:subject_id>/', views.SubjectLeaderboardView.as_view(), name='subject_leaderboard'),
    path('global/', views.GlobalLeaderboardView.as_view(), name='global_leaderboard'),
]
