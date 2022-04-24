from django.contrib import admin

from .models import Weather

class WeatherAdmin(admin.ModelAdmin):
   model = Weather
   ordering = ('applicable_date','created')
   list_display = ['applicable_date']

admin.site.register(Weather, WeatherAdmin)