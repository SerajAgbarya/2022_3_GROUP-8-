from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from app.tokens import generate_token
from cdfi import settings


def signup(request, signup_page_path, signin_page_name, email_template):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(username=username):
        #     messages.error(request, "Username already exist! Please try some other username.")
        #     return redirect('home')

        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email Already Registered!!")
        #     return redirect('home')

        # if len(username) > 20:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('home')

        # if pass1 != pass2:
        #     messages.error(request, "Passwords didn't matched!!")
        #     return redirect('home')

        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!!")
        #     return redirect('home')
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        messages.success(request,
                         "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
        subject = "Welcome to CDFI system!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to CDFI system! \nThank you for visiting us\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        # current_site = get_current_site(request)
        email_subject = "Confirm your Email @ CDFI Login!!"

        message2 = render_to_string(email_template, {
            'name': myuser.first_name,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect(signin_page_name)

    return render(request, signup_page_path)
