from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Answer
from django.http import JsonResponse
from .forms import QForm, AForm

# Create your views here.
def list_posts(request):
    posts = Post.objects.all()
    answers = Answer.objects.all()
    return render(request, "core/list_posts.html", {'posts': posts, 'answers': answers})

@login_required
def post_question(request):
    if request.method == "GET":
        form = QForm()
    else:
        form = QForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_posts')
    return render(request, 'core/post_question.html', {'form': form})

@login_required
def answer(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'GET':
        form = AForm()
    else:
        form = AForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.post = post
            
            form.save()
            return redirect(to='list_posts')
    return render(request, "core/answer.html", {"form": form, "post": post})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "core/post_details.html", {'post': post})

@login_required
def delete_post(request, pk):

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect(to='list_posts')
    return render(request, "core/delete_post.html", {"post": post})

@login_required
def correct_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if not answer.is_correct:
        answer.is_correct = True
        answer.save()
        data = {'change': 'correct'}
    else:
        answer.is_correct = False
        answer.save()
        data = {'change': 'not-correct'}
    return JsonResponse(data)


