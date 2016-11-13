from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


def home(request):
    return render(request, 'home.html')


class HelloView(View):

    def get(self, request):
        return HttpResponse("Hello world!!")