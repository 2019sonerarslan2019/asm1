from django.shortcuts import render
from .models import RevolvingDoor

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

    #--------------------------3
    
    #sabit kanat dograma
    ph = float(rd.trans_height) + 45
    if ph > float(int(ph))+.001: ph = int(ph) + 1

    pr = (float(rd.dia)-34)/2
    if pr > float(int(pr))+.001: pr = int(pr) + 1

    iydograma = (((float(rd.dia)-94)*3.14)/6)+15
    if iydograma > float(int(iydograma))+.001: iydograma = int(iydograma) + 1

    dydograma = (((float(rd.dia)-34)*3.14)/6)+15
    if dydograma > float(int(dydograma))+.001: dydograma = int(dydograma) + 1

    ik = ((((float(rd.dia)-94)*3.14)/6)+15)-108
    if ik > float(int(ik))+.001: ik = int(ik) + 1

    dk = ((((float(rd.dia)-34)*3.14)/6)+15)-108 
    if dk > float(int(dk))+.001: dk = int(dk) + 1

    #sabit kanat lamine cam
    ch = (float(rd.trans_height)+45)-73
    if ch > float(int(ch))+.001: ch = int(ch) + 1 

    cr = (float(rd.dia)-68)/2
    if cr > float(int(cr))+.001: cr = int(cr) + 1

    iycam = (((float(rd.dia)-86)*3.14)/6)-67
    if iycam > float(int(iycam))+.001: iycam = int(iycam) + 1
    
    dycam = (((float(rd.dia)-68)*3.14)/6)-67
    if dycam > float(int(dycam))+.001: dycam = int(dycam) + 1

    
    context = {
        'rd':rd,
        'ph':int(ph),'pr':int(pr),'ch':int(ch),
        'cr':int(cr),'iydograma':int(iydograma),'dydograma':int(dydograma),
        'iycam':int(iycam),'dycam':int(dycam),'ik':int(ik),'dk':int(dk),
    }
    
    return render(request,'revolving_door/detail-revolving-door.html',context)