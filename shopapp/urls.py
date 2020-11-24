from django.urls import path

from shopapp.views import *

app_name = 'shopapp'
urlpatterns = [
	path('home/',home,name='home'),
	path('market/',market,name='market'),
	path('cart/',cart,name='cart'),
	path('mine/',mine,name='mine'),
]