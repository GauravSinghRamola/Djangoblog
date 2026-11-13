# from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    # return HttpResponse("Hi this is working")
    return render(request, 'index.html')

