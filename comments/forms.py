# comments/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',) # 用户只需要填写内容
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}), # 让输入框小一点
        }
