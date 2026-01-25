from django.contrib import admin
from .models import StudentProfile, Lesson, Progress, QuizResult
# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(Lesson)
admin.site.register(Progress)
admin.site.register(QuizResult)