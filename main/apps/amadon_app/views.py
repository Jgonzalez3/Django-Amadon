# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
totalitems = 0
totalspent = 0
def index(request):
    return render(request, 'amadon_app/index.html')
def buy(request):
    # Below is the key for getting request.session[""] to equal something if there is nothing in the request.session[""]
    if "totalspent" not in request.session:
        request.session["totalspent"] = 0
        print request.session["totalspent"]
    if "totalitems" not in request.session:
        request.session["totalitems"] = 0

    context = {
        "1001": 19.99,
        "1002": 29.99,
        "1003": 4.99,
        "1004": 49.99,
    }
    print context
    price = 0
    if request.method == "POST":
        productid = request.POST['product_id']
        for product in context:
            if productid == product:
                price = context[product]
                print price
        quantity = request.POST["quantity"]
        totalprice = int(quantity) * price
        request.session["totalprice"] = totalprice
        totalquantity = int(quantity)
        # print "totalquantity", totalquantity
        # print "totalprice", totalprice
        # print type(totalquantity)
        # print "quantity", quantity
        request.session["totalspent"] += totalprice
        request.session["totalitems"] += totalquantity
        return redirect("/amadon_app/checkout")
def checkout(request):
    return render(request, "amadon_app/checkout.html")

def back(request):
    if request.method == "POST":
        request.session["totalprice"] = 0
        return redirect("/")
