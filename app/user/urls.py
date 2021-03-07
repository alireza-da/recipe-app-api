from django.urls import path
import user.views

app_name = 'user'

url_patterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
