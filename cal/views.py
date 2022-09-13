from django.shortcuts import render
from django.views.generic import View
# Create your views here.


# Create your views here.

class CalHome(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'cal_home.html', context)


class CalSuma(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'cal_suma.html', context)

class CalResultado(View):
    def get(self, request, *args, **kwargs):

        #va11 = int(request.GET["num1"])
        va11 = "num1"
        va12 = "num2"
        res = va11 + va12


        context= {
            'result': res
        }
        return render(request, 'cal_resultado.html', context)