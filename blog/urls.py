from django.urls import path
from . import views

app_name = 'blog' # 定义应用命名空间

urlpatterns = [
    # 首页，显示文章列表
    path('', views.PostListView.as_view(), name='post_list'),
    # 文章详情页，需要文章的 primary key (pk)
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # 创建新文章
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    # 编辑文章
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    # 删除文章
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
] 