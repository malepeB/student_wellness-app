from django import forms
from .models import Task, WellnessCheckin, StudyReminder, MoodJournalEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateTimeInput
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority']

class WellnessForm(forms.ModelForm):
    class Meta:
        model = WellnessCheckin
        fields = ['mood', 'journal_entry']  # ✅ Include journal
        widgets = {
            'journal_entry': forms.Textarea(attrs={'rows': 3}),
        }

class StudyReminderForm(forms.ModelForm):
    class Meta:
        model = StudyReminder
        fields = ['title', 'reminder_time']
        widgets = {
            'reminder_time': DateTimeInput(attrs={'type': 'datetime-local'})
        }

class StudentSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MoodJournalForm(forms.ModelForm):
    class Meta:
        model = MoodJournalEntry
        fields = ['mood', 'note']