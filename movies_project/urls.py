# movies_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# API (DRF)
from movies_app.views import DirectorViewSet, MovieViewSet

# Frontend (Bootstrap)
from movies_app import views_front

# Router para la API REST
router = routers.DefaultRouter()
router.register(r'directors', DirectorViewSet)   # /api/directors/ (CRUD)
router.register(r'movies', MovieViewSet)         # /api/movies/ (CRUD)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API REST (JSON + Browsable API)
    path('api/', include(router.urls)),

    # Frontend: dashboard con Directores y Películas en una sola página
    path('', views_front.dashboard, name='dashboard'),

    # Acciones desde los modales (editar/eliminar)
    path('directors/edit/<int:id>/', views_front.edit_director, name='edit_director'),
    path('directors/delete/<int:id>/', views_front.delete_director, name='delete_director'),

    path('movies/edit/<int:id>/', views_front.edit_movie, name='edit_movie'),
    path('movies/delete/<int:id>/', views_front.delete_movie, name='delete_movie'),
]
