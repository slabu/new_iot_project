from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Controler, Controler_record, Sensor


def chart(request):
    return render(request, 'devices/chart.html')

class DeviceChartView(DetailView):
    model = Controler
    context_object_name = 'controler'


class DeviceListView(ListView):
    model = Controler
    template_name = 'devices/controlers.html'
    context_object_name = 'controlers'


class SensorChartView(DetailView):
    model = Sensor
    template_name = 'devices/sensor_detail.html'
    context_object_name = 'sensor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(dir(context['object']))
        print(context['object'])
        object = context['object']

        print(object.id)

        new = Sensor.objects.filter(id=object.id).first()
        print(dir(new))
        print(dir(new.sensor_measure_set.values()))

        length_of_array = len(new.sensor_measure_set.values())

        chart_data = [[(i+1)*10, new.sensor_measure_set.values().order_by('datetime')[i]['measure']*10] for i in range(length_of_array)]


        print(chart_data)
        context['chart_data'] = chart_data[1:]
        context['start_coords'] = chart_data[0]
        print(context)
        return context
