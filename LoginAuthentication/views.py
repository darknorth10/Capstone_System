from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ForgotPassForm, LoginForm
from django.contrib import messages
from AuditTrail.models import AuditTrail
from django.contrib.auth.forms import PasswordChangeForm
from .models import CustomUser
import random
from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password


# Create your views here.

print('ok')
def login_page(request):

  form = LoginForm()
  message = ''

  if request.method == "POST":
    form = LoginForm(request.POST)

    if form.is_valid():
      user = authenticate(
        username = form.cleaned_data['username'],
        password = form.cleaned_data['password'],
        )

      if user is not None:
        login(request, user)
        messages.success(request, f'Welcome {request.user}, have a great day!')
        audit = AuditTrail(user=request.user, action=f'{request.user} has logged in.', location='Login Authentication')
        audit.save()
        return redirect('dashboard')
      else:
        print("Wrong username or pass")
        message = "Wrong username or password"
        form = LoginForm()
    else:
      form = LoginForm()

  return render(request, 'Login/login.html', context={'form': form, 'message': message})

#Logout view
def logout_user(request):
  audit_log = AuditTrail(user=request.user, action=f'{request.user} has logged out.', location='Login Authentication')
  audit_log.save()
  logout(request)
  message = "You've logged out."
  return render(request, 'Login/logout.html', context={'message':message})


def email_check(request):
  message = None
  if request.method == 'POST':
    username = request.POST.get('username')

    if CustomUser.objects.filter(username=username).exists():
      # check if user has email
      curr_user = CustomUser.objects.get(username=username)

      if curr_user.email is not None:
        #=====================Send OTP to Email =================#

        #otp generator
        otp = random.randint(100000, 999999)
        print(otp)

        cache.set('otp', otp, 30)
        curr_user.otp = cache.get('otp')

        # ================ send email =================
        a = cache.get('otp')

        send_mail(
          'Reset your Password',
            f'Here is your OTP {a} please do not share it with others.',
            '',
            [curr_user.email],
            fail_silently=False,
        )

        curr_user.save()

        return redirect('forgot_password', username)

      else:
        message = 'There is no email bounded to the account please contact your administrator.'


    else:
      message = 'Username does not exist'



  return render(request, 'Login/check_email.html', context={'error_message': message})

# forgot password
def forgot_password(request, username):

  if CustomUser.objects.filter(username=username).exists():
    changepassuser = CustomUser.objects.get(username=username)

  else:

    return redirect('check_email')


  form = ForgotPassForm()

  if request.method == 'POST':

    form = ForgotPassForm(request.POST)

    if form.is_valid():
      if form.cleaned_data['otp'] == changepassuser.otp:
        new_password = form.cleaned_data['password1']
        changepassuser.password = make_password(new_password)
        audit_log = AuditTrail(user=request.user, action=f'{changepassuser.username} has changed password through forgot password.', location='Login Authentication')
        audit_log.save()
        messages.success(request, 'Password has been changed successfully.')
        return redirect('login')

      else:
        messages.error(request, 'OTP is invalid or incorrect.')

      print(form.errors)


  context = {
    'form': form,
    'changeuser': changepassuser,
    }

  reset_user = CustomUser.objects.get(username=username)
  return render(request, 'Login/forgot_password.html', context)


def resend_otp(request, username):
        curr_user = CustomUser.objects.get(username=username)

    #=====================Send OTP to Email =================#
        #otp generator
        otp = random.randint(100000, 999999)


        if cache.get('otp') is not None:
          print(cache.get('otp'))
          messages.error(request, 'Error resending OTP, wait for 30 secods to resend.')

        else:

          cache.add('otp', otp, 30)
          a = cache.get('otp')
          curr_user.otp = cache.get('otp')
          curr_user.save()
          print(cache.get('otp'))

          send_mail(
            'Reset your Password',
            f'Here is your new OTP {a} please do not share it with others.',
            '',
            [curr_user.email],
            fail_silently=False,
          )

          messages.success(request, 'OTP has been resent successfully.')
        return redirect('forgot_password', username)