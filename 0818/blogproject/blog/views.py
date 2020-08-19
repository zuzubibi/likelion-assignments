from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects
    #블로그 모든 글들을 대상으로
    posts_list=Post.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(posts_list,3)
    #request된 페이지가 뭔지를 알아내고 ( request페이지를 변수에 담아냄 )
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts_num = paginator.get_page(page)

    return render(request,'home.html',{'blogs':posts,'posts':posts_num})



def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def new(request):
    return render(request, 'post/new.html')

def create10(request):
    ifake = Faker()
    for i in range(10):
        post = Post()
        post.title = ifake.name()
        post.body = ifake.sentence()
        post.pub_date = timezone.datetime.now()
        post.save()
    return redirect('/')

def delete(request, post_id):
    post_num = get_object_or_404(Post, pk=post_id)
    post_num.delete()
    return redirect('/')