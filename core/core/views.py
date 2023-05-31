from django.shortcuts import render
from store.models import Product, CoverPhoto

def home(request):
    products = Product.objects.all().filter(is_available=True)
    cover_image = CoverPhoto.objects.all()
    contex = {
        "products":products,
        "cover_image":cover_image
    }
    return render(request, "index.html", contex)