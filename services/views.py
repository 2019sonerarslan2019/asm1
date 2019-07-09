from django.shortcuts import render
from .models import RevolvingDoor
# Create your views here.
from .forms import RevolvingDoorForm


def revolving_door_view(request):
    
    rd = RevolvingDoor.objects.all()

    context = {
        'rd':rd,
    }

    return render(request,'revolving_door/revolving-door.html',context)


def create_revolving_door_view(request):
    if request.user.is_authenticated:

        form = RevolvingDoorForm(request.POST or None)

        if form.is_valid():
            form.save()
            

        context = {
            'form':form,
        }

    return render(request,'revolving_door/create-revolving-door.html',context)

def detail_revolving_door_view(request,id):
    
    rd = RevolvingDoor.objects.get(id=id)

    context = {
        'rd':rd,
    }
    return render(request,'revolving_door/detail-revolving-door.html',context)