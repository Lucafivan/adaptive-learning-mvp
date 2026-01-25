from django.db import models
from accounts.models import User
# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return self.user.email
    
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField()
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.order}. {self.title}"
    
class Progress(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.lesson}"
    
class QuizResult(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    score = models.FloatField()
    attempt = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.lesson} ({self.score})"