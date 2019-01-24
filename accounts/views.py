from django.shortcuts import render, redirect
from accounts.forms import UserForm
from accounts.models import UserProfile
from accounts.models import Transactions

# Create your views here.
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse




from django.contrib import messages
from django.contrib.auth import (authenticate,
                                 login,
                                 logout
                                 )
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import UserRegistrationForm
from .forms import Deposit_form
from .forms import Withdrawl_form
from .models import User




def home(request):
    return render(request, 'accounts/home.html')


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "accounts/login.html", context)
    else:
        return render(request, "accounts/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "accounts/success.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))





#
# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect("home")
#     else:
#         title = "Create a Bank Account"
#         form = UserRegistrationForm(
#             request.POST or None,
#             request.FILES or None
#             )
#
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data.get("password1")
#             user.set_password(password)
#             user.save()
#             new_user = authenticate(email=user.email, password=password)
#             login(request, new_user)
#
#             return redirect("home")
#
#         context = {"title": title, "form": form}
#
#         return render(request, "accounts/form.html", context)


def register_view(request):  
    if request.user.is_authenticated:
        return redirect("home")
    else:
        title = "Create a Bank Account"
        form = UserRegistrationForm(
            request.POST or None,
            request.FILES or None
            )

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            new_user = authenticate(email=user.email, password=password)
            login(request, new_user)

            return redirect("home")

        context = {"title": title, "form": form}

        return render(request, "accounts/form.html", context)

# def deposit(request):
#     if not request.user.is_authenticated:
#         return render(request, "accounts/login.html")
#     else:
#         form = Deposit_form(request.POST or None,
#                             request.FILES or None)
#
#         if form.is_valid():
#             request.user = form.save(commit= False)
#             deposit.user = request.user
#             deposit.user.balance += deposit.user.amount
#             deposit.user.save()
#             deposit.save()
#             return render(request, "accounts/account_details.html")
#
#     context = {
#         "form" : form
#     }
#     return render(request, "accounts/form.html", context)


def deposit(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        title = "Deposit"
        form = Deposit_form(request.POST or None,
                            request.FILES or None)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            # adds users deposit to balance.
            deposit.user.balance += deposit.amount
            deposit.user.save()
            deposit.save()
            messages.success(request, 'You Have Deposited {} $.'
                             .format(deposit.amount))
            return redirect("home")

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, "accounts/form.html", context)


def withdrawl(request):
    if not request.user.is_authenticated:
        raise Http404
    else:
        title = "Withdrawl"
        form = Withdrawl_form(request.POST or None)

        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user

            if withdrawal.user.balance >= withdrawal.amount:

                withdrawal.user.balance -= withdrawal.amount
                withdrawal.user.save()
                withdrawal.save()
                return redirect("home")

            else:
                return render(request, "Error You Can't Withdraw Please Return To Previous Page"
                )

        context = {
                    "title": title,
                    "form": form
                  }
        return render(request, "accounts/form.html", context)


@login_required(login_url="/login/")
def account_details(request):
    # if request.user.is_authenticated:
        return render(request, "accounts/account_details.html")






#
# def transact(request):
#     if not request.user.is_authenticated:
#         return redirect("home")
#     else:
#         transact_variable = [ "deposit", "withdrawl"]
#         if transact_variable == "deposit":
#             list1 = [balance, amount]
#             user = request.user
#             balance = sum(list1)
#             balance.save()
#         else:
#             user= request.user
#             x = subtraction(balance,amount)
#             balance.save()
#
#             context = {
#                 "user": user,
#                 "amount": amount,
#                 "balance": balance,
#                 "transact_variable": transact_variable,
#
#             }
#             return render(request, "accounts/transactions.html", context)

# def register_view(request):  # Creates a New Account & login New users
#     if request.user.is_authenticated:
#         return redirect("home")
#     else:
#         title = "Create a Bank Account"
#         form = UserRegistrationForm(
#             request.POST or None,
#             request.FILES or None
#             )
#
#         if form.is_valid():
#             user = form.save(commit=False)
#             password = form.cleaned_data.get("password1")
#             user.set_password(user.password)
#             user.save()
#             new_user = authenticate(email=user.email, password=password)
#             login(request, new_user)

#
#             return redirect("home")
#
#         context = {"title": title, "form": form}
#
#         return render(request, "accounts/form.html", context)

#
# def subtraction(x,y):
#     total = x - y
#     return total
#
#



# def withdrawl(request):
#     if not request.user.is_authenticated:
#         return Http404
#     else:
#         title = "Withdrawl"
#         form = Withdrawl_form(request.POST or None,
#                             request.FILES or None)
#         if form.is_valid():
#             request.user = form.save(commit= False)
#             withdrawl.user = request.user
#             withdrawl.user.balance -= withdrawl.amount
#             withdrawl.user.save()
#             withdrawl.save()
#             return render(request, "accounts/account_details.html")
#
#     context = {
#         "title" : title,
#         "form" : form
#     }
#     return render(request, "accounts/form.html", context)


# def emp(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('accounts/index.html')
#             except:
#                 pass
#     else:
#         form = UserForm()
#     return render(request,'accounts/index.html',{'form':form})
#
