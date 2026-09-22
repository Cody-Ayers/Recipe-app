# Recipe Manager Application

A Django web application that allows users to create, manage, and view recipes through a web interface. Users can store ingredients, cooking instructions, preparation times, recipe images, and recipe-related data within a centralized application.

## Live Application

🔗 https://codys-recipe-app-f140f86eb127.herokuapp.com/

---

# Project Overview

The Recipe Manager Application was built using Python and Django to provide a user-friendly platform for managing recipe information.

The application supports:

- User account creation and authentication
- Recipe creation and management
- Recipe image uploads
- Data reporting and visualization
- PostgreSQL production deployment
- Local SQLite development

---

# Technologies Used

## Backend

- Python 3.12
- Django 4.2
- Gunicorn

## Databases

### Production

- PostgreSQL

### Development

- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript

## Data Processing & Visualization

- Pandas
- NumPy
- Matplotlib

## Deployment & Version Control

- Heroku
- WhiteNoise
- Git
- GitHub

---

# Features

## User Accounts

- User registration
- User login
- User logout
- Account management

## Recipe Management

- Create recipes
- View recipe details
- Browse recipe collections
- Store ingredients
- Store cooking instructions
- Store preparation and cooking times
- Upload recipe images

## Reporting & Visualization

- Recipe reporting
- Recipe data visualization using Pandas and Matplotlib

## Media Management

- Upload recipe images
- Display uploaded recipe images

---

# Application Structure

```text
recipe_project/
│
├── recipe_project/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
│
├── recipes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── users/
│
├── media/
│   └── recipes/
│
├── staticfiles/
│
├── requirements.txt
├── Procfile
└── manage.py
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Cody-Ayers/Recipe-app.git
cd Recipe-app
```

## Create a Virtual Environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Apply Database Migrations

```bash
python manage.py migrate
```

## Create a Superuser

```bash
python manage.py createsuperuser
```

## Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

# Recipe Model

The application stores recipe information including:

```python
name
ingredients
description
cooking_time
pic
```

Recipe images are handled using Django's ImageField:

```python
pic = models.ImageField(
    upload_to='recipes',
    default='no-image.jpg'
)
```

---

# Production Environment

## Database Configuration

Production:

- PostgreSQL

Development:

- SQLite

## Environment Variables

```text
DATABASE_URL
DJANGO_SECRET_KEY
```

---

# Maintenance Activities

During ongoing development and deployment, the following maintenance work was completed:

- Upgraded Heroku stack from Heroku-22 to Heroku-24
- Upgraded Python runtime from 3.9 to 3.12
- Updated project dependencies
- Investigated deployment-related issues
- Restored recipe data in the PostgreSQL database
- Restored recipe image assets
- Updated media file configuration
- Tested application functionality following updates

---

# Deployment

The application is deployed using:

- Heroku-24
- Python 3.12
- PostgreSQL
- Gunicorn
- WhiteNoise

## Deploy Updates

```bash
git push heroku main
```

## View Logs

```bash
heroku logs --tail -a codys-recipe-app
```

---

# Technical Concepts Demonstrated

- Python Development
- Django Framework
- PostgreSQL
- SQLite
- User Authentication
- Database Migrations
- File Upload Handling
- Data Processing
- Data Visualization
- Cloud Deployment
- Application Maintenance
- Version Control
- Git & GitHub

---

# Future Improvements

- Recipe categories
- Search and filtering
- Favorites functionality
- Recipe sharing
- Cloud image storage
- Additional reporting features
- Responsive UI improvements
- REST API implementation

---

# Screenshots

Add screenshots after capturing images from the live application.

## Home Page

```text
screenshots/home.png
```

## Recipe List

```text
screenshots/recipes.png
```

## Recipe Details

```text
screenshots/details.png
```

## Reporting Dashboard

```text
screenshots/analytics.png
```

---

# Author

**Cody Ayers**

GitHub Profile:
https://github.com/Cody-Ayers

Repository:
https://github.com/Cody-Ayers/Recipe-app

Live Application:
https://codys-recipe-app-f140f86eb127.herokuapp.com/

---

# License

This project was developed as part of a software engineering portfolio and educational coursework.
