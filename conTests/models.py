from django.db import models
from django.conf import settings
from Edu.models import Subject, Exercise

User = settings.AUTH_USER_MODEL


class Contest(models.Model):
      subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
      name = models.CharField(max_length=255)
      start_time = models.DateTimeField()
      end_time = models.DateTimeField()
      duration = models.PositiveIntegerField(help_text="Duration in minutes")
      description = models.TextField(blank=True, null=True)

      def __str__(self):
            return self.name


class ContestExercise(models.Model):
      contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
      exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

      class Meta:
            unique_together = ('contest', 'exercise')


class ContestParticipant(models.Model):
      contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      finish_time = models.DateTimeField(null=True, blank=True)
      score = models.PositiveIntegerField(default=0)

      class Meta:
            unique_together = ('contest', 'user')


class ParticipantAnswer(models.Model):
      contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
      answer_text = models.TextField(blank=True, null=True)
      is_correct = models.BooleanField(default=False)
      answered_time = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f"{self.user} -> {self.exercise}"

