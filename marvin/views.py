from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.core.mail import send_mail

from .models import Post, Project
from .forms import PostForm, ProjectForm, ContactForm

def main_page(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    projects = Project.objects.filter(started_date__lte=timezone.now()).order_by('-started_date')
    return render(request, 'marvin/main_page.html', {'posts': posts, 'projects': projects})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Contact Form"
            from_email = form.cleaned_data['email']
            message = "From: " + from_email + "\n\n" + form.cleaned_data['message']
            
            send_mail(subject, message, from_email, ['mv@marvin.tech'], fail_silently=True)

            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'marvin/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'marvin/contact_success.html')

def post_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'marvin/post_page.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_page', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'marvin/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_page', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'marvin/post_edit.html', {'form': form})

def project_page(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'marvin/project_page.html', {'project': project})

def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.started_date = timezone.now()
            project.save()
            return redirect('project_page', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'marvin/project_edit.html', {'form': form})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('project_page', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'marvin/project_edit.html', {'form': form})