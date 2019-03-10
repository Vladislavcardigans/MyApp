from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainApp/homePage.html', )

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['If you have a questions, ask me by telefon', '(068) 0668-68-68', 'example@mail.ru']})