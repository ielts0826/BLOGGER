from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
# LoginRequiredMixin 用于限制只有登录用户才能访问
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from comments.forms import CommentForm # 导入评论表单
from comments.models import Comment # 导入评论模型

# Create your views here.

# 文章列表视图 (ListView)
class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html' # 指定模板
    context_object_name = 'posts' # 在模板中使用的变量名
    paginate_by = 5 # 每页显示 5 篇文章

# 文章详情视图 (DetailView)
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post' # 在模板中使用的变量名

    # 添加额外上下文到模板
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 获取这篇文章的所有评论
        context['comments'] = self.object.comments.all()
        # 如果用户已登录，则添加评论表单
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm()
        return context

    # 处理 POST 请求 (即用户提交评论)
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login') # 如果未登录，重定向到登录页

        self.object = self.get_object() # 获取当前文章对象
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False) # 创建评论对象，但不保存到数据库
            new_comment.post = self.object # 关联评论到当前文章
            new_comment.author = request.user # 设置评论作者为当前用户
            new_comment.save() # 保存评论到数据库
            # 成功后重定向回当前文章详情页
            return redirect(self.object.get_absolute_url())
        else:
            # 如果表单无效，重新渲染页面，并显示错误信息
            context = self.get_context_data()
            context['comment_form'] = form # 把包含错误的表单传回模板
            return self.render_to_response(context)

# 创建文章视图 (CreateView)
class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'category', 'tags'] # 允许用户填写的字段

    # 自动设置作者为当前登录用户
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # 成功创建后跳转到文章详情页 (利用模型中的 get_absolute_url)

# 编辑文章视图 (UpdateView)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'category', 'tags']

    # 只有文章作者才能编辑
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    # 成功更新后跳转到文章详情页 (利用模型中的 get_absolute_url)

# 删除文章视图 (DeleteView)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list') # 删除成功后跳转到文章列表

    # 只有文章作者才能删除
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
