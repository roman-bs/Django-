import logging

from django.shortcuts import render

from shop.models import Product

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.order_by("-id")
    return render(request, "products/list.html", {"products": products})


def product_view(request, slug):
    products = Product.objects.get(slug=slug)
    return render(request, "product/view.html", {"products": products})
