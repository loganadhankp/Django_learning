# Django Learning Environment

This directory contains a pre-configured Python virtual environment with Django and essential dependencies for learning.

---

## 🚀 Quick Start Guide

### 1. Activate the Virtual Environment

In **PowerShell**:
```powershell
.\.venv\Scripts\Activate.ps1
```
> *If you encounter a script execution error in PowerShell, allow scripts for the current session:*
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> .\.venv\Scripts\Activate.ps1
> ```

In **Command Prompt (CMD)**:
```cmd
.venv\Scripts\activate.bat
```

---

## 🛠️ Essential Django Commands

### Initialize a new project
To create a project in the current directory:
```bash
django-admin startproject myproject .
```
*(The `.` places `manage.py` in the current folder rather than nesting an extra subfolder).*

### Run Database Migrations
Django comes with default SQLite database support:
```bash
python manage.py migrate
```

### Create an Admin / Superuser
```bash
python manage.py createsuperuser
```

### Start the Local Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser. Access the admin dashboard at `http://127.0.0.1:8000/admin/`.

### Create a Django App
```bash
python manage.py startapp myapp
```

---

## 📦 Installed Packages

- **`django`** (5.2.x): Core web framework.
- **`pillow`**: Image processing library required for Django `ImageField`.
- **`python-dotenv`**: Reads `.env` files for managing secret keys and settings.
- **`django-debug-toolbar`**: Interactive debugging panel for inspecting queries, templates, and performance.
