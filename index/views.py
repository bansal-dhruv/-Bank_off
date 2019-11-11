from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
# Create your views her
from .models import *


def index(request):
    return render(request,'index.html')


@csrf_exempt
def login(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return dashboard(request)
        else:
            return render(request,'register.html')
    else:
        return render(request, 'login.html')

@csrf_exempt
def signup(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']

        new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,password=password)
        new_user.save()
        print("created")
        return login(request)
    else:
        return render(request, 'register.html')


def registerStartup(request):
    if request.method == 'POST':
        startup = request.POST.get('startup_name')
        description = request.POST.get('bio')
        password = request.POST.get('password')
        moneyNeeded = request.POST.get('money_needed')

        User_cand = models.startStartup.objects.create(startup=startup, username=request.user.username, password=password,
                                                       description=description, moneyNeeded=moneyNeeded, moneyBorrowed=0, Investors=0)
        User_cand.save()
        return redirect('/index')

    else:
        return render(request, 'register_startup.html')


def dashboard(request):
    z = startStartup.objects.all()
    zz = lendStartup.objects.all()
    username = request.user.username
    startuplist = {}
    for i in zz:
        if str(i.username) == username:
            startuplist["A"] = str(i.startup)
            startuplist["B"] = str(i.moneyLended)
    print(startuplist)
    return render(request, "dashboard.html", {'allStartup': z, 'investment': startuplist, 'username': username})


@csrf_exempt
def investStartup(request, startup):
    print("Invest")
    if request.method == "POST":
        print('yes')
        username = request.user.username
        moneyLend = request.POST.get('moneyLended')
        print('yes')
        z = startStartup.objects.filter(startup=startup)
        print(z[0])
        z=z[0]
        z.moneyNeeded = int(z.moneyNeeded) - int(moneyLend)
        z.moneyBorrowed = int(z.moneyBorrowed) + int(moneyLend)
        z.Investors += 1
        z.save()

        print('yes1')
        User_cand = lendStartup.objects.create(username=username, startup=startup, moneyLended=moneyLend)
        User_cand.save()
        return dashboard(request)

    else:
        return render(request, "Invest.html", {"data": {"startup": startup}})
