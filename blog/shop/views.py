import logging

from django.shortcuts import render

from shop.models import Product

logger = logging.getLogger(__name__)


def product_list(request):
    products = Product.objects.order_by("-id")
    return render(request, "products/list.html", {"products": products})


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "products/card.html", {"product": product})
