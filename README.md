# Recipe App

A full-stack Django web application that allows users to create, manage, and analyze recipes. Users can store ingredients, cooking instructions, preparation times, and images while tracking recipe information through an intuitive interface.

## Live Application

🔗 https://codys-recipe-app-f140f86eb127.herokuapp.com/

---

# Features

## User Authentication

- User registration
- Login and logout functionality
- User profile management
- Secure authentication system

## Recipe Management

- Create recipes
- View recipe details
- Browse recipe collection
- Store ingredients and cooking instructions
- Upload and display recipe images
- Automatically calculate recipe difficulty

## Data Visualization

- Recipe records dashboard
- Recipe statistics and analytics
- Visual reports generated with Pandas and Matplotlib

## Media Management

- Upload recipe images
- Display recipe photos
- Media file support for production deployment

---

# Technologies Used

## Backend

- Python 3.12
- Django 4.2

## Database

- PostgreSQL (Production)
- SQLite (Development)

## Frontend

- HTML5
- CSS3
- JavaScript

## Data Analysis

- Pandas
- Matplotlib
- NumPy

## Deployment

- Heroku-24
- Gunicorn
- WhiteNoise

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

## Clone Repository

```bash
git clone https://github.com/Cody-Ayers/Recipe-app.git
cd Recipe-app
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

### Mac/Linux

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

## Run Migrations

```bash
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Development Server

```bash
python manage.py runserver
```

Visit:

```text
http://127.0.0.1:8000
```

---

# Recipe Model

Example model fields:

```python
name
ingredients
description
cooking_time
pic
```

Images are uploaded using:

```python
pic = models.ImageField(
    upload_to='recipes',
    default='no-image.jpg'
)
```

---

# Production Environment

## Database

Production uses:

- Heroku PostgreSQL

Development uses:

- SQLite

## Environment Variables

```text
DATABASE_URL
DJANGO_SECRET_KEY
```

---

# Deployment

The application is deployed on Heroku using:

- Heroku-24 Stack
- Gunicorn
- PostgreSQL
- Python 3.12

Deploy updates:

```bash
git push heroku main
```

View logs:

```bash
heroku logs --tail -a codys-recipe-app
```

---

# Recent Maintenance & Recovery

This project recently underwent a full production maintenance and recovery effort including:

- Migration from Heroku-22 to Heroku-24
- Python upgrade from 3.9 to 3.12
- Dependency modernization
- PostgreSQL database recovery
- Restoration of 23 recipe records
- Recovery of recipe image assets
- Production media file configuration fixes
- Deployment validation and testing

---

# Future Improvements

- Recipe categories and tags
- Search and filtering
- Favorites functionality
- User recipe sharing
- Cloud image storage (AWS S3 or Cloudinary)
- Enhanced analytics dashboard
- Mobile-responsive UI improvements

---

# Screenshots

Add screenshots here after capturing images from the live application.

### Home Page

screenshots/home.png

### Recipe List

screenshots/recipes.png

### Recipe Details

screenshots/details.png

### Analytics Dashboard

screenshots/analytics.png

---

# Author

**Cody Ayers**

GitHub:
https://github.com/Cody-Ayers

Repository:
https://github.com/Cody-Ayers/Recipe-app

---

# License

This project was developed as part of a software engineering portfolio and educational coursework.
