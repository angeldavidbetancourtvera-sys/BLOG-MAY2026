from django.urls import path
from .views import PostListView, PostDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/nuevo/', BlogCreateView.as_view(), name='post-create'),
    path('post/actualizar/<int:pk>/', BlogUpdateView.as_view(), name='post-update'),
]
