from django.db import models
from django.contrib.auth.models import User
from blog.models import Post # 导入 Post 模型

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    class Meta:
        ordering = ['created_at'] # 按创建时间正序排列
