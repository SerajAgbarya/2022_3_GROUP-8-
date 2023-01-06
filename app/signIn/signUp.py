from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.core.mail import EmailMessage, send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from app.tokens import generate_token
from cdfi import settings


def signup(request, signup_page_path, signin_page_name, email_template, group_name=None):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            context["signup_error"] = "Username already exist! Please try some other username."

        if User.objects.filter(email=email).exists():
            context["signup_error"] = "Email Already Registered!!"

        if len(username) > 20:
            context["signup_error"] = "Username must be under 20 charcters!!"

        if pass1 != pass2:
            context["signup_error"] = "Passwords didn't matched!!"

        if not username.isalnum():
            context["signup_error"] = "Username must be Alpha-Numeric!!"

        if not context:
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

            # Get the username from the form
            # Get the group by name
            group = Group.objects.get(name=group_name)
            # Add the user to the group
            myuser.groups.add(group)
            return redirect(signin_page_name)

    return render(request, signup_page_path, context)
