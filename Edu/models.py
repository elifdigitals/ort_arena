from django.db import models


class Subject(models.Model):
      subject_name = models.CharField(max_length=255)
      description = models.TextField(blank=True, null=True)

      def __str__(self):
            return self.subject_name


class Topic(models.Model):
      subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
      topic_name = models.CharField(max_length=255)
      description = models.TextField(blank=True, null=True)

      def __str__(self):
            return f"{self.subject.subject_name}: {self.topic_name}"


class Exercise(models.Model):
      TYPE_CHOICES = [
            ('single', 'Single choice'),
            ('multiple', 'Multiple choice'),
            ('coding', 'Coding problem'),
      ]
      subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
      topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
      text = models.TextField()
      type = models.CharField(max_length=50, choices=TYPE_CHOICES)
      difficulty = models.PositiveIntegerField(default=1)
      points = models.PositiveIntegerField(default=0)

      def __str__(self):
            return f"{self.text[:50]}..."


class ExerciseTest(models.Model):
      exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='tests')
      input_data = models.TextField()
      expected_output = models.TextField()

      def __str__(self):
            return f"Test #{self.id} for {self.exercise}"
