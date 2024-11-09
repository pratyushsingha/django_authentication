# Django Authentication System

A robust authentication system built with Django, featuring social login integration (Google, Facebook, Twitter) and Cloudflare Turnstile protection.

![Project Demo](https://utfs.io/f/glvA31ChFgm4NWgRWFrm6qUSAZpXHL1xgvoTmsjCc0VFDw8K)

## Features

- 🔐 User Authentication
  - Email & Password Registration
  - Social Login (Google, Facebook, Twitter)
  - Password Reset
  - Session Management

- 🛡️ Security
  - Cloudflare Turnstile Protection
  - CSRF Protection
  - Secure Password Hashing
  - Environment Variables for Secrets

- 👤 User Management
  - User Profile
  - Account Settings
  - Session Control

- 🎨 UI/UX
  - Responsive Design
  - Clean & Modern Interface
  - Social Media Integration
  - Flash Messages
  - Form Validation

## Tech Stack

### Backend
- Python 3.10+
- Django 5.1.3
- django-allauth
- django-turnstile
- python-dotenv

### Security
- Cloudflare Turnstile
- Django Security Middleware
- CSRF Protection

## Local Setup

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/pratyushsingha/django_authentication

# Navigate into the repository directory
cd django_authentication

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Create .env file from example
cp .env.example .env

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (Optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`