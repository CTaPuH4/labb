from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.About.as_view(), name='about'),
    path('get_job/', views.GetJob.as_view(), name='get_job'),
    path('help/', views.Help.as_view(), name='help'),
]
