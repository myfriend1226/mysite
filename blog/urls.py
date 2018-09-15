from django.urls import path
from . import views


urlpatterns = [
    path("",views.index.as_view(),name='index'),
    path('blog/',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('blog/post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('blog/post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('blog/post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('blog/drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('blog/post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('blog/post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('blog/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('blog/comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('blog/comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
