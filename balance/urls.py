from django.urls import path, include
from balance import views
urlpatterns = [
    path('modules/', views.modules_view, name='modules'),
]
