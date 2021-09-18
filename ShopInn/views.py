from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Contact
from math import ceil

# Create your views here.
def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n / 4)
        allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds}
    return render(request,"ShopInn/index.html", params)

def about(request):
    return render(request,'ShopInn/about.html')

def contact(request):
        if request.method == "POST":
            print(request)
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            desc = request.POST.get('desc', '')
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
        return render(request, 'ShopInn/contact.html')

def tracker(request):
    return render(request, 'ShopInn/tracker.html')

def search(request):
    return HttpResponse("We are at search")

def productView(request , myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'ShopInn/productView.html', {'product': product[0], 'id': myid})

def checkout(request):
    return HttpResponse("We are at checkout")
