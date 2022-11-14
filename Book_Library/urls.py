"""Book_Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('show-books/', show_books, name="show_books"),  
    path('edit-book/<int:pk>/', edit_book, name="edit_book"),  
    path('hard-delete/<int:pk>/', hard_delete, name="hard_delete"),
    path('book-restore/<int:pk>',book_restore,name='book_restore'),
    path('active-books/',active_books,name="active_books"),
    path('inactive-books/',inactive_books,name="inactive_books"),
    
    # -------------------class based views
    path('cbv-home/',Home.as_view(),name='cbv_home'),
]
