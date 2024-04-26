from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('contact', views.contact, name='contact'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('buy_data', views.buy_data, name='buy_data'),
    path('buy_airtime', views.buy_airtime, name='buy_airtime'),
    path('fund_account', views.fund_account, name='views.fund_account'),


    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]