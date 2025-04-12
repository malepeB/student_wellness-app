
from django.urls import path
from .views import (
    login_view, signup_view, dashboard, logout_view,
    create_task, checkin_wellness, toggle_task,mood_journal,
    calendar_view, wellness_chart_view, add_reminder
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('checkin/', checkin_wellness, name='checkin_wellness'),
    path('toggle-task/<int:task_id>/', toggle_task, name='toggle_task'),
    path('calendar/', calendar_view, name='calendar'),
    path('wellness-chart/', wellness_chart_view, name='wellness_chart'),
    path('add-reminder/', add_reminder, name='add_reminder'),
    path('journal/', mood_journal, name='mood_journal'),
]

