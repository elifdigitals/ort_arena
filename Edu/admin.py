from django.contrib import admin
from .models import Subject, Topic, Exercise, ExerciseTest


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
      list_display = ('id', 'subject_name', 'description')
      search_fields = ('subject_name',)
      ordering = ('id',)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
      list_display = ('id', 'topic_name', 'subject', 'description')
      list_filter = ('subject',)
      search_fields = ('topic_name', 'subject__subject_name')
      ordering = ('subject', 'id')


class ExerciseTestInline(admin.TabularInline):
      """Показывает тесты прямо на странице упражнения"""
      model = ExerciseTest
      extra = 1


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
      list_display = ('id', 'text_short', 'subject', 'topic', 'type', 'difficulty', 'points')
      list_filter = ('subject', 'topic', 'type', 'difficulty')
      search_fields = ('text', 'subject__subject_name', 'topic__topic_name')
      inlines = [ExerciseTestInline]

      def text_short(self, obj):
            """Сокращает текст задания в списке"""
            return obj.text[:50] + ("..." if len(obj.text) > 50 else "")
      text_short.short_description = "Задание"


@admin.register(ExerciseTest)
class ExerciseTestAdmin(admin.ModelAdmin):
      list_display = ('id', 'exercise', 'input_data_short', 'expected_output_short')
      search_fields = ('exercise__text',)

      def input_data_short(self, obj):
            return obj.input_data[:30] + ("..." if len(obj.input_data) > 30 else "")
      input_data_short.short_description = "Входные данные"

      def expected_output_short(self, obj):
            return obj.expected_output[:30] + ("..." if len(obj.expected_output) > 30 else "")
      expected_output_short.short_description = "Ожидаемый результат"
