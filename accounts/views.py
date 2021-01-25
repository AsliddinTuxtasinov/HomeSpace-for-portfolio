from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import LoginForm, RegisterForm


# sign up
def sign_up(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST['email']
            username = register_form.cleaned_data['username']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']

            if password1 == password2:
                if User.objects.filter(username = username).exists():
                    messages.info(request, "username band")
                    return redirect('sign_up')

                elif User.objects.filter(email = email).exists():
                    messages.info(request, "bu email royhatdan o'tgan yoki xato kiritilgan")
                    return redirect('sign_up')

                else:
                    user = User.objects.create_user(
                        email = email,
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        password = password1
                    )
                    user.save()
                    # return redirect('../' + username)
            else:
                messages.info(request, 'parrollar bir biriga mos emas')
                return redirect('sign_up')
            return redirect('../../'+username)
    else:
        register_form = RegisterForm()
    return render(request,"accounts/sign_up.html", { 'form' : register_form })


# sign in
def sign_in(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = auth.authenticate(username = username, password = password)

            if user is not None:
                auth.login(request, user)
                return redirect('../../'+username)
            else:
                messages.info(request, "username yoki password noto'g'ti kiritilgan")
                return redirect("sign_in")
    else:
        login_form = LoginForm()
    return render(request,"accounts/sign_in.html", { 'form' : login_form })

def logout(request):
    auth.logout(request)
    return redirect('/')