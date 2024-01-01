from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib import messages
from .models import Article,Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def AllArticles(request):
    key = request.GET.get("keys")
    if key:
        articles = Article.objects.filter(title__contains=key)
        context = {
        "articles":articles
        }
        return render(request, "articles.html",context) 
   
    articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request, "articles.html",context)   

def Index(request):
    return render(request, "index.html")

def About(request):
    return render(request, "about.html")
@login_required(login_url="user:login")
def Dashboard (request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request, "dashboard.html",context)
@login_required(login_url="user:login")
def AddArticle (request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Eklendi")
        return redirect("article:dashboard")
     
    return render(request, "addarticle.html",{"form":form})

def DetailArticle(request,id):
    article = get_object_or_404(Article,id=id)
    comments = article.Comments.all()
    context = {
        "article":article,
        "comments":comments
    }
    return render(request,"article.html",context)
 
@login_required(login_url="user:login")
def UpdateArticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def DeleteArticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")
    return redirect("article:dashboard")

def AddCommentArticle(request,id):
    article = get_object_or_404(Article,id=id)
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
        messages.success(request,"Yorum Başarıyla Eklendi")
    
    return redirect(reverse("article:article",kwargs={"id":id}))
