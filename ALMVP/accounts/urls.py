from django.urls import path
from .views import RegisterView, DashboardView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('dashboard/', DashboardView.as_view()),
]