from django.shortcuts import render
from .models import RevolvingDoor

from .forms import RevolvingDoorForm
import math

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

def YUVARLA(x):

    if x > float(int(x)) + .001 :
        x = int(x) + 1 
        return x

    else: 
        return x    

    

def detail_revolving_door_view(request,id):
    
    rd = RevolvingDoor.objects.get(id=id)

    #--------------------------Kanopi

    us_dis = rd.canopy - 140 
    if rd.canopy > 210:
        us_dis = 70

    ts_dis_kesim = ((int(rd.dia)-4)*3.14)/2
    if ts_dis_kesim > float(int(ts_dis_kesim)) + .001: ts_dis_kesim = int(ts_dis_kesim) + 1    

    ts_dis_cap = int(rd.dia)- 4  

    us_dis_kesim =  ((int(rd.dia)-4)*3.14)/2
    if us_dis_kesim > float(int(us_dis_kesim)) + .001: us_dis_kesim = int(us_dis_kesim) + 1

    us_dis_cap = int(rd.dia) - 4   

    kanopi_birlesim = int(rd.canopy) - 53
    kbu_u_profile = int(rd.canopy) - 53
    sbu_u_profile = int(rd.canopy) - 78

    s1 = math.sqrt(((int(rd.dia)/2)-40)**2-(330**2)*2)
    if s1 > float(int(s1)+.001) : s1 = int(s1) + 1
    s2 = (int(rd.dia)/2)-345
    if s2 > float(int(s2)+.001) : s2 = int(s2) + 1
    s3 = ((int(rd.dia)/2)-355)-35
    if s3 > float(int(s3)+.001) : s3 = int(s3) + 1

    u_prf_dis_kesim = ((int(rd.dia)-94)*3.14)/2
    if u_prf_dis_kesim > float(int(u_prf_dis_kesim) + .001): u_prf_dis_kesim = int(u_prf_dis_kesim) + 1
    u_profile_dis_cap = int(rd.dia) - 94


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

    #---------------------4

    k1 = int(rd.trans_height) - 76
    dk = (int(rd.trans_height)-76)-22
    kb = int(rd.trans_height) - 76
    kl = (int(rd.dia)-244)/2
    if kl > float(int(kl))+.001: kl = int(kl) + 1
    ad = (int(rd.trans_height)-76)-156
    ch = (int(rd.trans_height)-76)-163
    cl = (int(rd.dia-244)/2)-94
    if cl > float(int(cl))+.001: cl = int(cl) + 1
    ek = ((int(rd.dia)-244)/2)-49   
    if ek > float(int(ek)) + .001: ek = int(ek) + 1
    k2 = (int(rd.dia)-244)/2
    if k2 > float(int(k2)) + .001: int(k2) + 1 

    #--------------------7
    #--------Levha 1    
    lb = 0
    if int(rd.dia) > 3600: lb = (((int(rd.dia)/2)-57.5)-487.5)
    else: lb = (int(rd.dia)-810)/2
    if lb > float(int(lb)) + .001 : lb = int(lb) + 1

    dy = ((((int(rd.dia)-115)*3.14)/12)+40)
    if dy > float(int(dy)) + .001 : dy = int(dy) + 1
    
    iy = ((695*3.14)/12)+40
    if iy > float(int(iy)) + .001 : iy = int(iy) + 1
    
    r2 =  (int(rd.dia)-115)/2 

    #--------Levha 2
    lb_2 = 0
    if int(rd.dia) > 3600: lb_2 = (((int(rd.dia)/2)-57.5)-487.5)
    else: lb_2 = (int(rd.dia)-810)/2
    lb_2 = YUVARLA(lb_2)

    dy_2 = ((((int(rd.dia)-115)*3.14)/12)+40)
    dy_2 = YUVARLA(dy_2)   

    iy_2 = ((695*3.14)/12)+40
    iy_2 = YUVARLA(iy_2)

    r2_2 =  (int(rd.dia)-115)/2
    
    sm = 0
    if int(rd.dia) > 3600: sm = (((int(rd.dia)-1090)/2)/2)-100
    else: sm = (((int(rd.dia)-810)/2)/2)-100     
    #---------Levha 3
    lb_3 = 0
    if int(rd.dia) > 3600: lb_3 = (((int(rd.dia)/2)-57.5)-487.5)
    else: lb_3 = (int(rd.dia)-810)/2
    lb_3 = YUVARLA(lb_3)
    dy_3 = ((((int(rd.dia)+242.5)+242.5)*3.14)/12)+40
    iy_3 =((695*3.14)/12)+40
    #(Dışçap-115)/2+5& " mm"
    r2_3 = ((int(rd.dia) -115)/2)+5

    context = {
        'rd':rd,
        'ph':int(ph),'pr':int(pr),'ch':int(ch),
        'cr':int(cr),'iydograma':int(iydograma),'dydograma':int(dydograma),
        'iycam':int(iycam),'dycam':int(dycam),'ik':int(ik),'dk':int(dk),'us_dis':int(us_dis),
        'ts_dis_kesim':int(ts_dis_kesim),'ts_dis_cap':int(ts_dis_cap),
        'us_dis_kesim':int(us_dis_kesim),'us_dis_cap':int(us_dis_cap),
        'kanopi_birlesim':int(kanopi_birlesim),'kbu_u_profile':int(kbu_u_profile),'sbu_u_profile':int(sbu_u_profile),
        's1':int(s1),'s2':int(s2),'s3':int(s3),'u_prf_dis_kesim':int(u_prf_dis_kesim),'u_profile_dis_cap':u_profile_dis_cap,
        'k1':int(k1),'dk':int(dk),'ad':int(ad),'kb':int(kb),'kl':int(kl),'ch':int(ch),'cl':int(cl),
        'ek':int(ek),'k2':int(k2),'lb':int(lb),'dy':int(dy),'iy':int(iy),'r2':float(r2),
        'lb_2':int(lb_2),'dy_2':int(dy_2),'iy_2':int(iy_2),'r2_2':float(r2_2),'sm':float(sm),
        'lb_3':int(lb_3),'dy_3':int(dy_3),'iy_3':int(iy_3),'r2_3':r2_3,



        
        
        
    }
    
    return render(request,'revolving_door/detail-revolving-door.html',context)