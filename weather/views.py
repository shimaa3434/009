from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org./data/2.5/weather?appid=c64ff127598966313352da0b06f96167&q='
    # api_key= 'c64ff127598966313352da0b06f96167'
    # api_url = 'https://api.openweathermap.org/data/2.5/weather'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        
    form = CityForm()

    cities = City.objects.all()

    weather_data = []
    if cities:

        for city in cities:
            data_url = url + str(city)

            response = requests.get(data_url).json()

            city_weather = {
                'city': city.name,
                'temperature': response['main']['temp'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
            }

            weather_data.append(city_weather)


    return render(request, 'weather/index.html', {'weather_data': weather_data, 'form': form})
    


