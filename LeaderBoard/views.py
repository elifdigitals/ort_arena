from django.shortcuts import render
from rest_framework import viewsets
from .models import Leaderboard
from .serializers import LeaderboardSerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all().order_by('-total_score')
    serializer_class = LeaderboardSerializer


from rest_framework import generics, permissions
from .models import Leaderboard, GlobalLeaderboard
from .serializers import LeaderboardSerializer, GlobalLeaderboardSerializer


class SubjectLeaderboardView(generics.ListAPIView):
    """Рейтинг по конкретному предмету"""
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Leaderboard.objects.filter(subject_id=subject_id).order_by('rank')


class GlobalLeaderboardView(generics.ListAPIView):
    """Общий рейтинг по всем предметам"""
    serializer_class = GlobalLeaderboardSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return GlobalLeaderboard.objects.all().order_by('global_rank')
