from django.urls import path
from .views import PostView

app_name = 'posts'

urlpatterns = [
    path('create/', PostView.as_view(), name='post_create'),
]