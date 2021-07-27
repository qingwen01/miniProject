# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
# from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
#
#
# from util.message import send_message
#
# import redis
# import random

class LoginView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        return Response({'status':True})

def hello(request):
    return HttpResponse("Hello world ! ")

def runoob(request):
    context = {'name':'haha','age':25,'sex':'女'}
    return render(request, 'templates/world.html', {"content":context})







# def phone_validators(value):
#
#
#
#
# class MessageSerializer(serializers.Serializers):
#     phone = serializers.CharField(label='手机号',validators=[phone_validators,])
#
#
# class MessageView(APIView):
#     def get(self,request,*args,**kwargs):
#         ser = MessageSerializer(data=request.query_params)
#         if not ser.is_valid():
#             return Response({'status':False,'message':'手机格式错误'})
#         phone = ser.validated_data.get('phone')
#
#         random_code = random.randint(1000,9999)
#         send_message(phone,random_code)


