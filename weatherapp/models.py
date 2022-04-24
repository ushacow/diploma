from django.db import models


class Weather(models.Model):
    id = models.BigIntegerField(primary_key=True)
    weather_state_name = models.CharField(max_length=200)
    wind_direction_compass = models.CharField(max_length=200)
    created = models.DateTimeField('date published')
    applicable_date = models.DateField(unique=True)
    min_temp = models.FloatField(default=0)
    max_temp = models.FloatField(default=0)
    the_temp = models.FloatField(default=0)
    def __str__(self):
        return 'Date {}'.format(self.applicable_date)
        # return 'Date {}: {} and {} wind with max temp = {}, min temp = {}, and the temp = {}'.format(self.applicable_date, self.weather_state_name, self.wind_direction_compass, self.max_temp, self.min_temp, self.the_temp)