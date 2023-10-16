from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def index(request):
    return render(request, 'index.html', context={'name': 'An Khang'})

def welcome(request):
    return HttpResponse('Hello')

class TestView(View):
    def get(self, request):
        return HttpResponse('Test')
    def post(self, request):
        pass

