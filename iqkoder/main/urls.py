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

]

