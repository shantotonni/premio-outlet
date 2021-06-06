from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from premioapp.notification_test import send_nofification_to_users
# Create your views here.


def redirect_url(request):
    return HttpResponseRedirect('/premio-outlet/')


def market_update(request):
    # from .models import Market,Outlet,Category
    # markets = Market.objects.all()
    # for market in markets:
    #     outlet = Outlet.objects.filter(market__id = market.id).first()
    #     if outlet:
    #         market.lat = outlet.lat
    #         market.lng = outlet.lng
    #         market.save() 
    #         print(market.lat,market.lng)

    # import csv
    # with open('/home/baset/Desktop/markets.csv', 'r') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         market = Market.objects.filter(name=row[0]).first()
    #         if market:
    #             if row[1] == 'A':
    #                 market.category_id = 1
    #             if row[1] == 'B':
    #                 market.category_id = 2
    #             if row[1] == 'C':
    #                 market.category_id = 3
    #             if row[1] == 'D':
    #                 market.category_id = 4
    #             market.save()
    #             print(row[1],market.category_id)

    return HttpResponse("done")

def send_test_notification(request):
    result = send_nofification_to_users('test',['YCB14'],'Neoronta (Rx Update)','this is test notification')
    return HttpResponse("sent")

    