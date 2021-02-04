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
            user = auth.authenticate(username = username, password = password1)
            auth.login(request, user)
            return redirect('../../'+username)
    else:
        register_form = RegisterForm()
    return render(request,"accounts/sign_up.html", { 'form' : register_form })

# sign up second method

# def sign_up(request):
#     if request.method == 'POST':
#         regist_form = RegisterForm(request.POST)
#         if register_form.is_valid():
#             email = register_form.cleaned_data['email']
#             username = register_form.cleaned_data['username']
#             first_name = register_form.cleaned_data['first_name']
#             last_name = register_form.cleaned_data['last_name']
#             password1 = register_form.cleaned_data['password1']
#             password2 = register_form.cleaned_data['password2']
#             mycontext = dict
#             errorflag = False
#             errors = []

#             if password1 == password2:
#                 if User.objects.filter(username=username).exists():
#                     errorflag = True
#                     errormsg = "username band"
#                     errors.append(errormsg)

#                 elif User.objects.filter(email=email).exists():
#                     errorflag = True
#                     errormsg = "email band"
#                     errors.append(errormsg)
#                 elif errorflag != True:
#                     user = User.objects.create_user(
#                         username = username,
#                         email = email,
#                         first_name = first_name,
#                         last_name = last_name,
#                         password = password1
#                     ).save()
#                 else:
#                     mycontext["error"]=errorflag
#                     mycontext["errors"]=errors
#                     return redirect('sign_up',context)
#             else:
#                 errorflag = True
#                 errormsg = "parollar bir biriga mos emas"
#                 errors.append( errormsg )
#                 mycontext["error"]=errorflag
#                 mycontext["errors"]=errors
#                 return redirect('sign_up',context=mycontext)



#             user = auth.authenticate(username = username, password = password1)
#             auth.login(request, user)
#             return redirect('../'+username)

#     else:
#         regist_form = RegisterForm()
#     return render(request,"accaounts/sign_up.html", { 'form' : regist_form})




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