from datetime import datetime
from .models import *
from .forms import DateForm
from django.shortcuts import render


menu = ["UX/UI дизайнер"]

def about(request):
    result = Mein.objects.all().filter(title="UX/UI дизайнер")
    context = {
        'posts': result,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'about.html',  context=context)

def demand(request):
    return render(request, 'demand.html', {'menu': menu, 'title': 'Восстребованность профессии'})

def geografy(request):
    return render(request, 'geografy.html', {'menu': menu, 'title': 'География профессии'})

def skillvac (request):
    return render(request, 'skillvac.html', {'menu': menu, 'title': 'Необходимые навыки для профессии'})

def lastvacv (request):
   # form = forms.DateForm
    if request.method == 'POST':
        form = DateForm(request.POST)
        str_date = request.POST.get("decem_day")
        result = Date.objects.all().filter(published_at=datetime.strptime(str_date, "%Y-%m-%d").date())

    else:
        result = None
        str_date = ""

    context = {
        'posts': result,
        'menu': menu,
        'title': 'Последние вакансии',
        'cat_selected': 0,
        'decem_day': str_date
    }

    return render(request, 'lastvacv.html', context=context)







