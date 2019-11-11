from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="login"),
    path('dashboard/', views.dashboard),
    path('lend/<slug:startup>/', views.investStartup),
    path('registerstartup/', views.registerStartup),
    # path('/user',views.user,name="user")
]