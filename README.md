# 🧠 Student Wellness App 📚

A context-aware student assistant web application designed to support **academic planning** and **mental wellness tracking**. Built with Django, this planner-inspired system allows students to manage assignments, reminders, wellness check-ins, and mood tracking all in one place.

> ⏰ Last updated: April 12, 2025

---

## 🎯 Metaphor & Design

The app uses the **"Planner" metaphor** — acting as a digital assistant for students, similar to a notebook or personal diary. It helps organize life around class schedules, emotional check-ins, and productivity goals.

---

## ✨ Key Features

- ✅ **Dashboard Overview**
  - Displays tasks, class schedules, study reminders, wellness check-ins
  - Includes pie chart (task completion) & bar graph (weekly mood)
- 📆 **Calendar View**
  - See assignment due dates and plan ahead
- 📋 **Assignment Tracker**
  - Add, view, and complete assignments with deadlines
- ⏰ **Study Reminders**
  - Set reminders with date/time (uses calendar input)
- 😊 **Wellness Check-ins**
  - Rate daily mood; trends are visualized
- 🧠 **Mood Journal (Optional)**
  - Record and view personal thoughts over time
- 🔐 **User Authentication**
  - Sign up & login screens with password visibility toggle
- 📱 **Consistent UI Design**
  - Navigation bar persists across pages
  - Fully responsive with modern styling

---

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/malepeB/student_wellness-app.git
cd student_wellness-app

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Make migrations & run the server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
