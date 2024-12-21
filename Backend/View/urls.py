from django.urls import path
from .views import fetch_and_save_jobs


urlpatterns = [
    path('api/fetch-jobs/', fetch_and_save_jobs, name='fetch-jobs'),
]