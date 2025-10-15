from django.contrib import admin
from .models import Contest, ContestParticipant, ParticipantAnswer, ContestExercise, UserRating



@admin.register(UserRating)
class UserRatingAdmin(admin.ModelAdmin):
      list_display = ('user', 'rating', 'rank')
      search_fields = ('user__username',)



class ContestExerciseInline(admin.TabularInline):
      model = ContestExercise
      extra = 1


class ContestParticipantInline(admin.TabularInline):
      model = ContestParticipant
      extra = 0
      readonly_fields = ('score',)


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
      list_display = ('name', 'subject', 'contest_type', 'start_time', 'end_time', 'duration', 'total_exercises')
      list_filter = ('contest_type', 'subject')
      search_fields = ('name', 'subject__subject_name')
      inlines = [ContestExerciseInline, ContestParticipantInline]


@admin.register(ContestParticipant)
class ContestParticipantAdmin(admin.ModelAdmin):
      list_display = ('user', 'contest', 'score', 'finish_time')
      list_filter = ('contest',)
      search_fields = ('user__username', 'contest__name')


@admin.register(ParticipantAnswer)
class ParticipantAnswerAdmin(admin.ModelAdmin):
      list_display = ('user', 'contest', 'exercise', 'is_correct', 'answered_time')
      list_filter = ('contest', 'is_correct')
      search_fields = ('user__username', 'exercise__text')
