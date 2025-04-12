from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class WellnessCheckin(models.Model):
    MOOD_CHOICES = [('sad', '😞 Sad'), ('neutral', '😐 Neutral'), ('happy', '😊 Happy')]
    WELLNESS_CHOICES = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    wellness_level = models.CharField(max_length=10, choices=WELLNESS_CHOICES)
    journal_entry = models.TextField(blank=True)
class StudyReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    reminder_time = models.DateTimeField()

    def __str__(self):
        return self.title

class MoodJournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=10, choices=WellnessCheckin.MOOD_CHOICES)
    note = models.TextField()
