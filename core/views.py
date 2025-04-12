from cProfile import label
import json
from optparse import Values
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.utils.dateformat import DateFormat
from datetime import date

from .models import Task, WellnessCheckin, StudyReminder, MoodJournalEntry
from .forms import TaskForm, WellnessForm, StudyReminderForm, StudentSignupForm,MoodJournalForm
import json


from django.db.models import Count
from django.utils import timezone
from .models import Task, WellnessCheckin, StudyReminder

@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    completed_tasks = tasks.filter(completed=True).count()
    total_tasks = tasks.count()

    reminders = StudyReminder.objects.filter(user=request.user).order_by('reminder_time')
    
    # For Mood Chart
    checkins = WellnessCheckin.objects.filter(user=request.user).order_by('-date')[:7]
    wellness_labels = [checkin.date.strftime('%a') for checkin in reversed(checkins)]
    wellness_values = [checkin.mood for checkin in reversed(checkins)]

    latest_mood = checkins[0].mood if checkins else None

    today = timezone.now().date()
    upcoming_tasks = tasks.filter(due_date__gte=today).order_by('due_date')

    return render(request, 'core/dashboard.html', {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'total_tasks': total_tasks,
        'reminders': reminders,
        'wellness_labels': wellness_labels,
        'wellness_values': wellness_values,
        'latest_mood': latest_mood,
        'upcoming_tasks': upcoming_tasks,
        'today': today,
    })




def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = StudentSignupForm()
    return render(request, 'core/signup.html', {'form': form})


@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'core/create_task.html', {'form': form})


@login_required
def checkin_wellness(request):
    if request.method == 'POST':
        form = WellnessForm(request.POST)
        if form.is_valid():
            checkin = form.save(commit=False)
            checkin.user = request.user
            checkin.save()
            return redirect('dashboard')
    else:
        form = WellnessForm()
    return render(request, 'core/checkin_wellness.html', {'form': form})


@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = StudyReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('dashboard')
    else:
        form = StudyReminderForm()
    return render(request, 'core/add_reminder.html', {'form': form})


@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('dashboard')


@login_required
def calendar_view(request):
    tasks = Task.objects.filter(user=request.user, due_date__isnull=False).order_by('due_date')
    return render(request, 'core/calendar.html', {
        'tasks': tasks,
        'today': date.today(),
    })


@login_required
def wellness_chart_view(request):
    checkins = WellnessCheckin.objects.filter(user=request.user).order_by('date')
    dates = [DateFormat(checkin.date).format('M j') for checkin in checkins]
    levels = [checkin.wellness_level for checkin in checkins]

    return render(request, 'core/wellness_chart.html', {
        'dates': dates,
        'levels': levels
    })
@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = StudyReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('dashboard')
    else:
        form = StudyReminderForm()
    return render(request, 'core/add_reminder.html', {'form': form})
@login_required
def mood_journal(request):
    form = MoodJournalForm(request.POST or None)
    if form.is_valid():
        entry = form.save(commit=False)
        entry.user = request.user
        entry.save()
        return redirect('dashboard')
    return render(request, 'core/mood_journal.html', {'form': form})