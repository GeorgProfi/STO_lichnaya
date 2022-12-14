from django.shortcuts import render, redirect
from .models import list_of_executed
from .forms import ListForm


# Create your views here.


def index(request):

    if request.method == 'POST':
        if 'buy_btn' in request.POST:
            deleted_instance = list_of_executed.objects.filter(id=request.POST.get('buy_btn'))
            deleted_instance.delete()
    buy = list_of_executed.objects.all()
    return render(request, 'main/index.html', {'buy': buy})

def about(request):
    man = list_of_executed.objects.all()
    return render(request, 'main/about.html', {'man': man})


def list_E(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Global')
        else:
            error = 'форма не верна'
    form = ListForm()
    context = {
        'form': form
    }
    return render(request, 'main/list_E.html', context)
