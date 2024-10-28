from django.urls import path

from . import views

app_name = 'tours'

urlpatterns = [
    path('', views.TourListView.as_view(), name='index'),
    path('tours/<int:pk>/', views.TourDetailView.as_view(), name='detail'),
    path('profile/<slug:username>/', views.profile_detail, name='profile'),
]
