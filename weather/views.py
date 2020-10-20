import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=b5fbc38b68ebe3b05eb0a099c64a668c'
    city = 'London'

    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'weather/weather.html')
