from django.urls import path    
from . import views

urlpatterns = [
     path('', views.home, name="home"),
     path('contents/', views.contents, name="contents"),

     path('continents/', views.continents, name='continents'),
     path('add_continent/', views.add_continent, name='add-continent'),
     path('show_continent/<continent_id>', views.show_continent, name='show-continent'),
     path('update_continent/<continent_id>', views.update_continent, name='update-continent'),
     path('delete_continent/<continent_id>', views.delete_continent, name='delete-continent'),

     path('countries/', views.countries, name='countries'),
     path('add_country/', views.add_country, name='add-country'),
     path('show_country/<country_id>', views.show_country, name='show-country'),
     path('update_country/<country_id>', views.update_country, name='update-country'),
     path('delete_country/<country_id>', views.delete_country, name='delete-country'),


]

