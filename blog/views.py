from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class BlogHome(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'blog_home.html', context)

class BlogNosotros(View):
    def get(self, request, *args, **kwargs):
        context= {

        }
        return render(request, 'blog_nosotros.html', context)

class BlogServicios(View):
    def get(self, request, *args, **kwargs):
        context= {}
        return render(request, 'blog_servicios.html', context)