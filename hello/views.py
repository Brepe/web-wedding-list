from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
import os
import json
from gettingstarted import *
import socket

# Create your views here.
def index(request):
    # times = int(os.environ.get('TIMES',3))
    products_types = ['Eletrodomésticos', 'Móveis', 'Cama_mesa_e_banho', 'Utensílios_cozinha', 'Utilidades']
    products_array = []

    print("init")

    with open('hello/products.json', encoding='utf-8') as json_file:
        data = json.load(json_file)
    for p in data:
        products_array.append(p)

    print("end")
    return render(request, "index.html", {"products_types": products_types, "products_array": products_array})



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
