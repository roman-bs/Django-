"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import static as static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from posts.views import posts_index
from blog.views import register, image_upload_view
from homework.views import homework_index
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts_index),
    path('homework/', homework_index),
    path('register/', register),
    path('upload/', image_upload_view),
    path("api/", include(
        "api.urls", namespace="api"
    )),
]






if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
