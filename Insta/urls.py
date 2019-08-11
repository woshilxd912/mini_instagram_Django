from django.urls import path
from Insta.views import HelloDjango, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, addLike

urlpatterns = [
    path('test/', HelloDjango.as_view(), name='helloworld'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('like', addLike, name='addLike'),
]
