# PROJECT_1
Projects Overview
1. api_project

A beginner-friendly Django REST Framework project to build APIs for managing books.

Technologies: Django, Django REST Framework

Features:

List, create, update, and delete books

CRUD operations using ViewSets and Routers

Token authentication for API security

Directory: api_project/

Key Files:

models.py – Book model

serializers.py – BookSerializer

views.py – BookList, BookViewSet

urls.py – API routing

2. advanced-api-project

A more advanced Django project demonstrating custom serializers, nested relationships, and filtering.

Technologies: Django, Django REST Framework, django-filter

Features:

Author and Book models with nested serializers

CRUD operations with generic views

Filtering, searching, and ordering on API endpoints

Custom validation for Book publication year

Directory: advanced-api-project/

Key Files:

models.py – Author and Book models

serializers.py – Custom nested serializers

views.py – Generic views for CRUD

urls.py – API routing

3. django_blog

A Django project for creating a blogging platform.

Technologies: Django

Features:

Post model with title, content, author, and published_date

User-authored content with Django’s built-in User model

Base templates and static files for UI

Directory: django_blog/

Key Files:

models.py – Post model

Templates & static files for frontend

4. social_media_api

A full-featured social media API project with user authentication, posts, comments, follows, notifications, and likes.

Technologies: Django, Django REST Framework, Token Authentication

Features:

Custom User model with profile, followers, and following

Posts and Comments with CRUD operations

Like and Notification systems

User feed from followed users

Permissions to secure endpoints

Directory: social_media_api/

Key Files:

accounts/models.py – CustomUser model

accounts/serializers.py – User registration and login serializers

posts/models.py – Post and Comment models

posts/views.py – ViewSets for posts/comments

notifications/models.py – Notification model
