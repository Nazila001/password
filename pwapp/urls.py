from .views import user, pages
from django.urls import path

urlpatterns = [
    path('', user.as_view()),
    path('<int:pk>/', pages.as_view()),
]
