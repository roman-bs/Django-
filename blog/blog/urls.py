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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from blog.views import register
from posts.views import post_list, post_add, post_view, post_admin
from profiles.views import profiles_index
from shop.views import product_list, product_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", post_list, name="home"),
    path("post/admin/", post_admin, name="post_admin"),
    path("post/<str:slug>/", post_view, name="post_view"),
    path("posts/add/", post_add, name="post_add"),
    path("products/", product_list, name="product_list"),
    path("product/<str:slug>/", product_view, name="product_view"),
    path("profiles/", profiles_index, name="profiles_index"),
    path("register/", register, name="register"),
    path("api/", include("api.urls", namespace="api")),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)