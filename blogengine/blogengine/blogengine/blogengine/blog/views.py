
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.generic import TemplateView


from .models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

def posts_list (request):
    posts = Post.objects.all().order_by('-date_pub')
    return render (request, 'blog/index.html', context ={'posts' : posts})

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'

    #def get(self,request, slug):
        #post= Post.objects.get(slug__iexact= slug)
    #    post = get_object_or_404(Post, slug__iexact= slug)
    #    return render (request, 'blog/post_detail.html', context = {'post' : post})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context = {'form': form})

    #def get(self, request, slug):
    #    post = Tag.objects.get(slug__iexact=slug)
        #tag = get_object_or_404(Tags, slug__iexact= slug)
    #    return render (request, 'blog/tag_detail.html', context = {'tag': tag})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context = {'tags': tags})
