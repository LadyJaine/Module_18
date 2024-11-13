from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    items = {'Игры': ['Описание игры 1',
             'Описание игры 2',
             'Описание игры 3']
             }
    return render(request, 'fourth_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'fourth_task/cart.html')

def shop(request):
    return render(request, 'fourth_task/shop.html')




# Create your views here.
