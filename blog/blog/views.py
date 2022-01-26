from django.shortcuts import render, redirect
import logging
from django.contrib.auth.models import User

from blog.forms import RegisterForm
from .forms import ImageForm

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process validated data
            logger.info(form.cleaned_data)
            # form.cleaned_data["password"]
            user = User(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )


            user.set_password(form.cleaned_data['password'])

            user.save()


            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})