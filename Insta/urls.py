from django.urls import path
from Insta.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
]