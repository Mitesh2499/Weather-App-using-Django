import  requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
# Create your views here.



def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=913ef1b776bb023672fbbc6219afd08d'

    if request.method == "POST":
        city=request.POST['name']
        r = requests.get(url.format(city)).json()
        msg= r['message']
        Display=''
        if msg == 'city not found':
            Display=msg
            pass
        else:
            Display='Added new City'
            form=CityForm(request.POST)
            form.save()

    form = CityForm()
    cities=City.objects.all()
    weather_data=[]



    for city in cities:
        r=requests.get(url.format(city)).json()


        city_weather={
            'city': r['name'],
            'temp':r['main']['temp'],
            'dis':r['weather'][0]['description'],
            'icon':r['weather'][0]['icon']
        }

        weather_data.append(city_weather)


    context={'weather_data' : weather_data,'form':form}

    return  render(request,'weather/index.html',context)