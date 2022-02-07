from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Continents

from .forms import ContinentForm
# from .forms import ContinentForm

# Home
def home(request):
    return render(request, 'main/home.html', {})

# Contents
def contents(request):
    return render(request, 'main/contents.html', {})

# Continents
def continents(request):
    # If you want order desc then use -continent_rs or randomize ... put only ? 
    continents_list = Continents.objects.all().order_by('continent_sr')
    return render(request, 'continents/continents.html', {
                        "continents_list": continents_list 
    })

# # Add a continent
def add_continent(request):
    submitted = False
    if request.method == 'POST':
        form = ContinentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_continent?submitted=True')

    else:
            form = ContinentForm
            if 'submitted' in request.GET:
                submitted=True

    return render (request, 'continents/add_continent.html', {
                                                    'form': form,
                                                    'submitted': submitted, })    

# show a continent
def show_continent(request, continent_id):
    continent = Continents.objects.get(pk=continent_id)
    return render(request, 'continents/show_continent.html', {
                                            'continent': continent, })

# Update a continent
def update_continent(request, continent_id):
    continent = Continents.objects.get(pk=continent_id)
    form = ContinentForm(request.POST or None, instance=continent)
    if form.is_valid():
        form.save()
        return redirect('continents')

    return render(request, 'continents/update_continent.html', {
                                            'continent': continent, 
                                            'form' : form })

# Delete a continent
def delete_continent(request, continent_id):
    continent = Continents.objects.get(pk=continent_id)
    continent.delete()
    return redirect('continents')


           




