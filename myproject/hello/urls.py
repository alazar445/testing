from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_create, name='person_create'),
    path('success/', views.success, name='success'),  # this line is critical!
]
