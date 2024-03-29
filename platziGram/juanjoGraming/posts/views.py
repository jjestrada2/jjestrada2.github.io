""" Posts views"""
#Django imports
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
#utilities
from datetime import datetime
#models
from posts.models import Post
#forms
from posts.forms import PostForm
#Creo Diccionario de Posts



@login_required
def list_posts(request):
    """List existing posts."""
    posts=Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})



@login_required
def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form=PostForm()
    return render(
        request=request,
        template_name='posts/new.html',
        context={
        'form': form,
        'user':request.user,
        'profile':request.user.profile,}
    )    