import datetime
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from weatherapp.models import Weather
from django.template import loader

remote_api_base_url = "https://www.metaweather.com/api/location/"
weather_location_id = "2122265" # Moscow


def index(request):

    try:
        start_date_str = request.GET['start_date']
        start_date = datetime.date.fromisoformat(start_date_str)
    except:
        start_date = datetime.date.today() + datetime.timedelta(-30)
        start_date_str = start_date.strftime('%Y-%m-%d')

    try:
        end_date_str = request.GET['end_date']
        end_date = datetime.date.fromisoformat(end_date_str)
    except:
        end_date = datetime.date.today() + datetime.timedelta(+1)
        end_date_str = end_date.strftime('%Y-%m-%d')

    action = "filter"
    try:
        action = request.GET['action']
    except:
        pass
    if (action == 'load'):
        counter = start_date
        delta = datetime.timedelta(days=1)
        while counter <= end_date:
            # print(counter.strftime("%Y-%m-%d"))
            applicable_date = counter.strftime("%Y-%m-%d")
            full_url = remote_api_base_url + weather_location_id + '/' + applicable_date.replace('-','/')
            # print(counter)
            # print(applicable_date)
            # print(applicable_date.replace('-','/'))
            response = requests.get(full_url)
            json_response = response.json()
            weather_stub = Weather(weather_state_name="", wind_direction_compass="", applicable_date=datetime.date.fromisoformat(applicable_date.replace('/','-')))
            counter += delta

            max_temp_found = False
            min_temp_found = False
            the_temp_found = False
            for item in json_response:
                # print(item)
                weather_stub.id = item['id']
                weather_stub.weather_state_name = item['weather_state_name']
                weather_stub.wind_direction_compass = item['wind_direction_compass']
                weather_stub.created = item['created']
                if (not max_temp_found and item['max_temp']):
                    weather_stub.max_temp = round(item['max_temp'],3)
                    max_temp_found = True
                if (not min_temp_found and item['min_temp']):
                    weather_stub.min_temp = round(item['min_temp'],3)
                    min_temp_found = True
                if (not the_temp_found and item['the_temp']):
                    weather_stub.the_temp = round(item['the_temp'],3)
                    the_temp_found = True
                if (max_temp_found and min_temp_found and the_temp_found):
                    break
            try:
                weather_stub.save()
                update_status = "Data was successfully updated"
            except:
                update_status = "There was an error in update process"

    else:
        pass

    weather_list = Weather.objects.filter(applicable_date__gte=start_date).filter(applicable_date__lte=end_date).order_by('applicable_date')

    template = loader.get_template('weather/index.html')
    context = {
        'weather_list': weather_list,
        'start_date': start_date_str,
        'end_date': end_date_str,
    }

    return HttpResponse(template.render(context, request))