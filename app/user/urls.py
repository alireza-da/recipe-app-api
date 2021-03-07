from django.urls import path
import views

app_name = 'user'

url_patterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
