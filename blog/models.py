from django.db import models
from django.contrib.auth.models import User
from django.views.generic import DetailView

class Category(models.Model):
    name = models.CharField(max_length=225)

class Post(models.Model):
    image = models.ImageField(upload_to= 'blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    title = models.CharField(max_length=225)
    content = models.TextField()
    #tags
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.id}'
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        try:
            context['prev_post'] = post.get_previous_by_published_date()
        except Post.DoesNotExist:
            context['prev_post'] = None

        try:
            context['next_post'] = post.get_next_by_published_date()
        except Post.DoesNotExist:
            context['next_post'] = None

        return context