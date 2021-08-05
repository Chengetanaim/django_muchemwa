from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'designs/index.html')




def tshirts(request):
    return render(request, 'designs/tshirts.html')


def jeans(request):
    return render(request, 'designs/jeans.html')


def shoes(request):
    return render(request, 'designs/shoes.html')