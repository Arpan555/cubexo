from django.shortcuts import render,redirect
from django.http import HttpResponse
from testapp.models import UserProfile, History
from django.contrib import messages
import decimal

# Create your views here.
def home(request):
#     if request.session.get('email'):
#         return redirect('/profile')
    return render(request,'testapp/home.html')
def about(request):
    return render(request,"testapp/about.html")
def contact(request):
    return render(request,"testapp/contact.html")
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserProfile.objects.get(email=email)
            if user.password == password:
                request.session['email']=user.email
                return redirect('profile')
            else:
                messages.error(request,"Incorrect Password")
                return redirect('login')
        except UserProfile.DoesNotExist:
            messages.error(request,"User Does Not Exist Please Register First")
            return redirect('login')
    return render(request,"testapp/login.html")

def profile(request):
    email = request.session.get('email')
    
    if  not email:
        return redirect('login')
    user = UserProfile.objects.get(email=email)
    return render(request,'testapp/profile.html',{'username':user.name,'balance':user.balance})


def logout(request):
    request.session.flush()
    return redirect('/login')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mob_no = request.POST.get('mob_no')
        password = request.POST.get('password')
        UserProfile(name=name,email=email,mob_no=mob_no,password=password).save()
        messages.success(request,"Account Created Successfully")
        return redirect('login')
    return render(request,'testapp/register.html')

def credit(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        additional_msg = request.POST.get('additional_msg')
        email = request.session.get('email')
        user = UserProfile.objects.get(email=email)
        amount = decimal.Decimal(float(amount))
        newbalance = amount + user.balance
        History(amount=amount,status='Credit',additional_msg=additional_msg,user=user).save()
        UserProfile.objects.filter(email=email).update(balance=newbalance)
        messages.success(request,'Amount Credited Successfully')
        return redirect('profile')

    return HttpResponse("Server Error!")

def debit(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        additional_msg = request.POST.get('additional_msg')
        email = request.session.get('email')
        user = UserProfile.objects.get(email=email)
        amount = decimal.Decimal(float(amount))
        if amount > user.balance:
            messages.error(request,'Insufficient Balance')
            return redirect('profile')
        newbalance = user.balance - amount
        History(amount=amount,status='Debit',additional_msg=additional_msg,user=user).save()
        UserProfile.objects.filter(email=email).update(balance=newbalance)
        messages.success(request,'Amount Credited Successfully')
        return redirect('profile')

    return HttpResponse("Server Error!")


def history(request):
    email = request.session.get('email')
    user = UserProfile.objects.get(email=email)
    history = user.history_set.all()
    count = user.history_set.count()
    return render(request,'testapp/history.html',{'user':user,'count':count})