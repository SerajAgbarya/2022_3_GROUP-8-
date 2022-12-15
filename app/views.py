from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'index.html')

def manager_signin(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

    return render(request, 'manager-signin.html')
