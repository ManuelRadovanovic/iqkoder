from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Continents, Countries

from .forms import ContinentForm, CountryForm

# Paginator
from django.core.paginator import Paginator


# Home
def home(request):
    return render(request, 'main/home.html', {})

# Contents
def contents(request):
    return render(request, 'main/contents.html', {})

# Continents
def continents(request):  
    # if you want order desc then use -continent_rs or randomize... just put ?
    continents_list = Continents.objects.all().order_by('continent_sr')
    return render(request, 'continents/continents.html', {
                        "continents_list": continents_list })

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

# ----------------------------------------------------------------------------

# Countries
def countries(request):
    # If you want order desc then use -country_rs or randomize ... put only ? 
    countries_list = Countries.objects.all().order_by('country_sr')
    # Set up Pagination
    p = Paginator(countries_list, 2)
    page = request.GET.get('page')
    pcountries = p.get_page(page)
    nums = "a" * pcountries.paginator.num_pages
    return render(request, 'countries/countries.html', {
                        "countries_list": countries_list,
                        "pcountries": pcountries,
                        "nums" : nums  })

# # Add a country
def add_country(request):
    submitted = False
    if request.method == 'POST':
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_country?submitted=True')

    else:
            form = CountryForm
            if 'submitted' in request.GET:
                submitted=True

    return render (request, 'countries/add_country.html', {
                                                    'form': form,
                                                    'submitted': submitted, })    

# show a country
def show_country(request, country_id):
    country = Countries.objects.get(pk=country_id)
    return render(request, 'countries/show_country.html', {
                                            'country': country, })

# Update a country
def update_country(request, country_id):
    country = Countries.objects.get(pk=country_id)
    form = CountryForm(request.POST or None, instance=country)
    if form.is_valid():
        form.save()
        return redirect('countries')

    return render(request, 'countries/update_country.html', {
                                            'country': country, 
                                            'form' : form })

# Delete a country
def delete_country(request, country_id):
    country = Countries.objects.get(pk=country_id)
    country.delete()
    return redirect('countries')



           




