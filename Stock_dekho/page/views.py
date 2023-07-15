from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader

from .fetch_data import fetch
from .ticker import stock
import json 

# Create your views here.
def main(request):
   template = loader.get_template('main.html')
   stocks= stock().to_json(orient="records")
   context = {
      "stocks" : json.loads(stocks)
   }

   return HttpResponse(template.render(context,request))

def view_detail(request):
  
    searchWord = request.POST['result']
    print(searchWord)
    stock = fetch(searchWord)
    data = {
              "Date": stock[0],
              "Open": stock[1],
              "High": stock[2],
              "Low": stock[3],
              "Close": stock[4],
              "52High": stock[5],
              "52Low": stock[6],

    }
  
    return JsonResponse(data)
def chart(request):
   template = loader.get_template('plot.html')
   return HttpResponse(template.render({"d":1},request))