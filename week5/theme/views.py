from django.views.generic. base import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ThemeForm, CommentForm, HashtagForm
from .models import Theme, Comment, Hashtag
from django.utils import timezone 


class MainpageView(TemplateView):
    template_name = 'theme/main.html'

# Create your views here.
def detail(request, theme_id, comment=None):
        theme = get_object_or_404(Theme, id=theme_id)
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.theme_id = theme
                comment.comment_text = form.cleaned_data["comment_text"]
                comment.save()
                return redirect("detail", theme_id)
        else:
            form = CommentForm(instance=comment)    
            return render(request, "theme/detail.html", {"theme": theme, "form": form})

def commentedit(request, theme_id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return detail(request, theme_id, comment)


def commentremove(request, theme_id, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', theme_id)


def themeform(request, theme=None):
    if request.method == 'POST':
        form = ThemeForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            theme = form.save(commit=False)
            theme.published_at = timezone.now()
            theme.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = ThemeForm(instance=theme)
        return render(request,'theme/new.html' , {'form':form})

def hashtagform(request, hashtag=None):
    if request.method == 'POST':
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다."
                return render(request, 'theme/hashtag.html', {'form':form, "error_message":error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
                return redirect('home')
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'theme/hashtag.html', {'form':form})

def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    return render(request, 'theme/search.html', {'hashtag':hashtag}) 

def edit(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    return themeform(request,theme)

def remove(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    theme.delete()
    return redirect('home')

def main(request):
    return render(request, 'theme/main.html')

def home(request):
    theme = Theme.objects
    hashtags = Hashtag.objects
    return render(request, 'theme/home.html', {'theme':theme, 'hashtags':hashtags})

def new(request):
    return render(request, 'theme/new.html')

def create(request):
    theme= Theme()
    theme.title = request.GET['title']
    theme.body = request.GET['body']
    theme.published_at = timezone.datetime.now()
    theme.save()
    return redirect('/theme/home/')