from rest_framework import serializers
from .models import Leaderboard, GlobalLeaderboard

class LeaderboardSerializer(serializers.ModelSerializer):
      username = serializers.CharField(source='user.username', read_only=True)
      subject_name = serializers.CharField(source='subject.subject_name', read_only=True)

      class Meta:
            model = Leaderboard
            fields = ['id', 'username', 'subject_name', 'total_score', 'rank']


class GlobalLeaderboardSerializer(serializers.ModelSerializer):
      username = serializers.CharField(source='user.username', read_only=True)

      class Meta:
            model = GlobalLeaderboard
            fields = ['id', 'username', 'total_score', 'global_rank']
