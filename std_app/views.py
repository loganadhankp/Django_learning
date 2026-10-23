from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'id': 100,
        'name': 'loganaadhanhari',
        'email': 'loganaadhanhari@gmail.com',
        'age': 22,
    }

    return render(request, 'student.html', {'mydata': data})


def products_list(request):
    product = [
        {
            'id': 101,
            'name': 'laptop',
            'price': 50000,
            'quantity': 3,
        },
        {
            'id': 102,
            'name': 'laptop',
            'price': 55000,
            'quantity': 3,
        },
        {
            'id': 103,
            'name': 'laptop',
            'price': 60000,
            'quantity': 3,
        },
    ]

    return render(request, 'product.html', {'product': product})
def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'home.html')
def base(request):
    return render(request, 'base.html')