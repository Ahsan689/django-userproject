from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.http import JsonResponse
from .models import  UserData, Subscribe
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .serializers import UserDataSerializer

# Create your views here.

# def index(request):
#     if request.user.is_anonymous:
#         return redirect('/')
#     return render(request, 'index.html')

# def login(request):
#     if request.method=="POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         #check if user entered correct credentials
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             # A backend authenticated the credentials
#             return redirect('/')
#         else:
#             # No backend authenticated the credentials
#             return render(request, 'login.html')

#     return render(request, 'login.html')


# def logout (request):
#      return render(request, 'index.html')

# def subscribers(request):
#     subscribers = Subscribe.objects.values('email', 'date_submitted')
#     data = {
#         'subscribers' : list(subscribers)
#     }
#     return JsonResponse(data)

@csrf_exempt
def postUser(request):
    if request.method=="POST":

        data={}
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        userdetail = Subscribe(fname=fname, lname=lname )
        userdetail.save()
        # data["success"] = "subscribed Successfully"
        # return messages.success(request, "subscribed Successfully")
        return JsonResponse(userdetail)


def userDetail(request):
        detail = Subscribe.objects.values('id','fname', 'lname')
        data = {
            'userData' : list(detail)
        }
        return JsonResponse(data)

class UserDataViewSet(viewsets.ModelViewSet):
    queryset = UserData.objects.all().order_by('id')
    serializer_class = UserDataSerializer

@api_view(['POST',])
def post_data(request):
    serializer = UserDataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_data(request,id):
    userid = UserData.objects.get(id = id)
    print('userid---',userid)
    serializer = UserDataSerializer(userid, request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

# @api_view(['DELETE'])
# def delete_data(request,id):
#     userid = UserData.objects.get(id = id)
#     print('userid---',userid)
#     serializer = UserDataSerializer(userid, request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)
