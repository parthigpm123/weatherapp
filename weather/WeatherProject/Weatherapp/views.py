from django.shortcuts import render
import requests
import datetime

# Create your views here.
def home(request):
      
      if 'city' in requests.POST:
            city = requests.POST['city']
      else:
            city = 'indore'
                 
      url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=599292d69a88ba0df3c167f0826e343a'
      PARAMS = {'units':'metric'}
      
      data = requests.get(url,PARAMS).jason()
      
      description = data['weather'][0]['description']
      icon= data['weather'][0]['icon']
      temp=data['main']['temp']
      
      
      return render(request, 'Weatherapp/index.html')
