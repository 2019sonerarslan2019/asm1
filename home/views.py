from django.shortcuts import render

def home_view(request):

    return render(request,'home.html',{})


def view_401(request):

    return render(request,'401.html',{})