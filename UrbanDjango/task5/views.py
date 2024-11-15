from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse


# Create your views here.
def sign_up_by_django(request):
    info = {}
    users = {'Petrov':'hgffkjgyuyd', 'Ivanov':'jhgfrgsedtyguh', 'Sidorov':'gfdrtyuhtyuikj', 'Fedorov':'hfjfjdhdhry', 'Tuchkin':'fdhfhjdf'}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password == repeat_password and age >= 18 and username not in users:
                info['message'] = f'Приветствуем, {username}!'

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            if age < 18:
                info['error'] = 'Вы должны быть старше 18'

            if username in users:
                info['error'] = f'Пользователь {username} уже существует'
        else:
            info['error'] = 'Некорректные данные в форме'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request,'fifth_task/form_example.html',{'info':info})





def sign_up_by_html(request):
    users = {'Petrov':'hgffkjgyuyd', 'Ivanov':'jhgfrgsedtyguh', 'Sidorov':'gfdrtyuhtyuikj', 'Fedorov':'hfjfjdhdhry', 'Tuchkin':'fdhfhjdf'}
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        print(type(age))
        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f'Приветствуем, {username}!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        if age < 18:
            info['error'] = 'Вы должны быть старше 18'

        if username in users:
            info['error'] = f'Пользователь {username} уже существует'



    return render(request,'fifth_task/registration_page.html',{'info':info})

