from django.db import models
from django.conf import settings
from django.utils import timezone
from Edu.models import Subject, Exercise

User = settings.AUTH_USER_MODEL


class UserRating(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      rating = models.FloatField(default=1000)
      contests_participated = models.PositiveIntegerField(default=0)
      rank = models.CharField(max_length=50, default="Newbie")  

      def __str__(self):
            return f"{self.user} ({self.rating})"

      def update_rank(self):
            if self.rating < 1200:
                  self.rank = "Newbie"
            elif self.rating < 1400:
                  self.rank = "Pupil"
            elif self.rating < 1600:
                  self.rank = "Specialist"
            elif self.rating < 1800:
                  self.rank = "Expert"
            elif self.rating < 2000:
                  self.rank = "Candidate Master"
            elif self.rating < 2200:
                  self.rank = "Master"
            elif self.rating < 2400:
                  self.rank = "International Master"
            elif self.rating < 2600:
                  self.rank = "Grandmaster"
            elif self.rating < 3000:
                  self.rank = "International Grandmaster"
            else:
                  self.rank = "Legendary Grandmaster"
            self.save()


class Contest(models.Model):
      CONTEST_TYPE_CHOICES = [
            ('training', 'Training'),
            ('official', 'Official'),
      ]

      subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
      name = models.CharField(max_length=255)
      contest_type = models.CharField(max_length=20, choices=CONTEST_TYPE_CHOICES, default='training')
      start_time = models.DateTimeField()
      end_time = models.DateTimeField()
      duration = models.PositiveIntegerField(help_text="Duration in minutes")
      description = models.TextField(blank=True, null=True)

      def __str__(self):
            return f"{self.name} ({self.get_contest_type_display()})"

      def is_active(self):
            now = timezone.now()
            return self.start_time <= now <= self.end_time

      def total_exercises(self):
            return self.exercises.count()

      def update_scores(self):
            """Пересчитать очки участников"""
            participants = ContestParticipant.objects.filter(contest=self)
            for participant in participants:
                  score = ParticipantAnswer.objects.filter(
                  contest=self, user=participant.user, is_correct=True
                  ).aggregate(models.Sum('exercise__points'))['exercise__points__sum'] or 0
                  participant.score = score
                  participant.save()

      def update_ratings(self):
            """После завершения официального контеста пересчитать рейтинги"""
            if self.contest_type != 'official':
                  return

            participants = ContestParticipant.objects.filter(contest=self).order_by('-score', 'finish_time')
            if not participants:
                  return

            total = participants.count()

            for rank_position, participant in enumerate(participants, start=1):
                  user_rating, _ = UserRating.objects.get_or_create(user=participant.user)

                  # Упрощённая логика изменения рейтинга
                  delta = int(100 * (1 - (rank_position - 1) / total))
                  if rank_position > total * 0.7:  # нижние 30% теряют очки
                        delta = -int(50 * ((rank_position - total * 0.7) / (total * 0.3)))

                  user_rating.rating += delta
                  user_rating.update_rank()


class ContestExercise(models.Model):
      contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name='exercises')
      exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

      class Meta:
            unique_together = ('contest', 'exercise')

      def __str__(self):
            return f"{self.exercise} ({self.contest})"


class ContestParticipant(models.Model):
      contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      finish_time = models.DateTimeField(null=True, blank=True)
      score = models.PositiveIntegerField(default=0)

      class Meta:
            unique_together = ('contest', 'user')

      def __str__(self):
            return f"{self.user} in {self.contest}"

      def rank(self):
            participants = ContestParticipant.objects.filter(contest=self.contest).order_by('-score', 'finish_time')
            for i, p in enumerate(participants, start=1):
                  if p == self:
                        return i
            return None
      def update_scores(self):
            self.score = sum(ans.exercise.points for ans in self.participantanswer_set.filter(is_correct=True))
            self.save()



class ParticipantAnswer(models.Model):
      contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
      answer_text = models.TextField(blank=True, null=True)
      is_correct = models.BooleanField(default=False)
      answered_time = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return f"{self.user} -> {self.exercise}"

      def check_correctness(self):
            from Edu.models import ExerciseTest
            tests = ExerciseTest.objects.filter(exercise=self.exercise)
            passed = all(test.expected_output.strip() == self.answer_text.strip() for test in tests)
            self.is_correct = passed
            self.save()
            return passed
