from django.contrib import admin
from django.urls import path,include
from hfcapp  import views

urlpatterns = [
    path('',views.index,name='index'),
    path('more_gallery',views.more_gallery,name='service'),
    path('morepackage',views.morepackage,name='morepackage'),
    path('paymenta/<int:myid>',views.paymenta,name='payment'),
    path('paymentas/<int:myid>',views.paymentas,name='paymentas'),
]
