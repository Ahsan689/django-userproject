from turtle import home
from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from home import views

# router = routers.DefaultRouter()
# router.register(r'UserData', views.UserDataViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('post_val/', views.post_data, name='post_val'), # need to implement
    path('update_val/<id>', views.update_data, name='update_val'),
    # path('delete_val/<id>', views.delete_data, name='delete_val'),
    # path('', views.index, name = "home"),
    # path('login', views.login, name = "login"),
    # path('logout', views.logout, name = "logout"),
    # path('v1/subscribers', views.subscribers, name='subscribers'), # GET API
    # path('v1/subscribe/', views.subscribe, name='subscribe'), # POST API
    path('userDetail', views.userDetail, name='userDetail'), # GET API
    path('postUser', views.postUser, name='postUser'), # POST API

]