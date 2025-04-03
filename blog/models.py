from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # 用于生成 URL

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # auto_now_add=True 表示只在创建时设置时间
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True 表示每次保存对象时都更新时间
    updated_at = models.DateTimeField(auto_now=True)
    # ForeignKey 表示一对多关系，一个用户可以有多篇文章
    # on_delete=models.CASCADE 表示当用户被删除时，其文章也一并删除
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # ForeignKey 表示一篇文章属于一个分类
    # null=True, blank=True 表示分类是可选的
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    # ManyToManyField 表示多对多关系，一篇文章可以有多个标签
    # blank=True 表示标签是可选的
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    # 定义获取文章详情页 URL 的方法，方便在模板中使用
    def get_absolute_url(self):
        # 'blog:post_detail' 是 URL 的名字 (我们稍后定义)
        # kwargs={'pk': self.pk} 传递文章的主键 (id)
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    class Meta:
         # 默认按创建时间倒序排列
        ordering = ['-created_at']
