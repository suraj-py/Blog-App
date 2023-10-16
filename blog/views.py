from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'blogs_post_list'

# By default DetailView will provide
# a context object we can use in our template called either object or the
# lowercased name of our model, which would be post .
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
