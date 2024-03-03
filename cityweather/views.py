from django.shortcuts import render
import requests
# Create your views here.
from .models import City
from .forms import CityForm
def index(request):
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = CityForm()
    url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=923d71e68a6ca92603406f1b023e8108'
    cities = City.objects.all()
    weather_data = []
    for city in cities:
        
        city_weather = requests.get(url.format(city)).json()
   
        weather = {
             'city' : city,
             'temperature' : city_weather['main']['temp'],
             'description' : city_weather['weather'][0]['description'],
             'icon' : city_weather['weather'][0]['icon']
                   }
        weather_data.append(weather)
    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'cityweather/index.html', context) #returns the index.html template
