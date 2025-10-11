from django.db import models
from django.conf import settings
from Edu.models import Subject
from authUser.models import CustomUser

User = settings.AUTH_USER_MODEL



class Leaderboard(models.Model):
      """Рейтинг по каждому предмету"""
      user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
      subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
      total_score = models.BigIntegerField(default=0)
      rank = models.PositiveIntegerField(default=0)

      class Meta:
            unique_together = ('user', 'subject')
            ordering = ['rank']

      def __str__(self):
            return f"{self.user.username} — {self.subject.subject_name}: {self.total_score} pts"


class GlobalLeaderboard(models.Model):
      """Общий рейтинг по всем предметам"""
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      total_score = models.BigIntegerField(default=0)
      global_rank = models.PositiveIntegerField(default=0)

      class Meta:
            ordering = ['global_rank']

      def __str__(self):
            return f"{self.user.username} — total {self.total_score} pts"

