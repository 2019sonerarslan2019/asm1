from django.shortcuts import render,redirect,get_object_or_404
from .models import RevolvingDoor
from .forms import RevolvingDoorForm
import math
###################Pdf
from django.views.generic import View
from django.template.loader import get_template
from django.http import HttpResponse
from myapp.utils import render_to_pdf

class GeneratePDF(View):

    def get(self,request,id,*args,**kwargs):

        rd_pdf = get_object_or_404(RevolvingDoor,id=id)

        template = get_template('other/invoice.html')
        context = {
            'id':id,
            'rd_pdf':rd_pdf,
        }
        html = template.render(context)
        pdf = render_to_pdf('other/invoice.html',context)

        if pdf:
            response = HttpResponse(pdf,content_type="application/pdf") 
            filename = "%s_%s.pdf"%(str(rd_pdf.company),str(rd_pdf.id))
            content = "inline ; filename=''%s" %(filename)
            response['Content-Disposition'] = content   
            return response
        return HttpResponse('Not found')

def revolving_door_view(request):
    
    if request.user.is_authenticated:

    
        rd = RevolvingDoor.objects.all()

        context = {
            'rd':rd,
        }

        return render(request,'revolving_door/revolving-door.html',context)
    else:
        return redirect('401')

def create_revolving_door_view(request):
    if request.user.is_authenticated:

        form = RevolvingDoorForm(request.POST or None)

        if form.is_valid():
            form.save()

            return redirect('revolvingdoor')
            

        context = {
            'form':form,
        }

        return render(request,'revolving_door/create-revolving-door.html',context)
    else:
        return redirect('401')

def YUVARLA(x):

    if x > float(int(x)) + .001 :
        x = int(x) + 1 
        return x

    else: 
        return x    

    

def detail_revolving_door_view(request,id):
    
    rd = get_object_or_404(RevolvingDoor,id=id)

    if request.user.is_authenticated:
        #-------------------------Is Emri
        total_height = rd.trans_height + rd.canopy

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

        s1 = math.sqrt(((rd.dia/2)-40)**2-(330**2))*2
        s1 = YUVARLA(s1)        
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
        #(((ÇAP-34)*3,14)/6)+15-108
        dk_3 = ((((rd.dia-34)*3.14)/6)+15)-108 
        dk_3 = YUVARLA(dk_3)

        #sabit kanat lamine cam
        ch_sabit_kanat = (rd.trans_height+45)-73
        ch_sabit_kanat = YUVARLA(ch_sabit_kanat)

        cr = (float(rd.dia)-68)/2
        if cr > float(int(cr))+.001: cr = int(cr) + 1

        iycam = (((float(rd.dia)-86)*3.14)/6)-67
        if iycam > float(int(iycam))+.001: iycam = int(iycam) + 1
        
        dycam = (((float(rd.dia)-68)*3.14)/6)-67
        if dycam > float(int(dycam))+.001: dycam = int(dycam) + 1

        #---------------------4

        k1 = int(rd.trans_height) - 76
        dk_4 = (int(rd.trans_height)-76)-22
        kb = int(rd.trans_height) - 76
        kl = (int(rd.dia)-244)/2
        kl = YUVARLA(kl)
        ad = (int(rd.trans_height)-76)-156
        ch = (int(rd.trans_height)-76)-163
        cl = (int(rd.dia-244)/2)-94
        cl = YUVARLA(cl)
        ek = ((int(rd.dia)-244)/2)-49   
        ek = YUVARLA(ek)
        k2 = (int(rd.dia)-244)/2
        k2 = YUVARLA(k2)

        #--------------------7
        #--------Levha 1    
        lb = 0
        if int(rd.dia) > 3600: lb = (((int(rd.dia)/2)-57.5)-487.5)
        else: lb = (int(rd.dia)-810)/2
        lb = YUVARLA(lb)

        dy = ((((int(rd.dia)-115)*3.14)/12)+40)
        dy = YUVARLA(dy)
        
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
        dy_3 = ((((int(rd.dia)+242.5)+242.5)*3.14)/12)+70
        iy_3 =((695*3.14)/12)+40
        r2_3 = ((int(rd.dia) -115)/2)+5

        #-------8
            
        r_radus_8 = (int(rd.dia)-10)/2

        if int(rd.dia) <= 3000:
            lb_le = True
        else:
            lb_le = False

        lb = 0
        le = 0
        
        if lb_le:
            lb = int(rd.dia)-10
            le = ((int(rd.dia)-10)/2)+20   
        
        le_2 = int(rd.canopy) + 30          
        lb_2 = (((((rd.dia*3.14)/6)+400)/10)*10)

        #--------------3001 - 3501 ARASI
        lb1_3001 = math.sqrt((((rd.dia-10)/2)**2)-(960**2))*2
        lb2_3001 =  (((rd.dia-10)/2)+20)
        lb3_3001 = math.sqrt((((rd.dia-10)/2)**2)-(980**2))+20
        lb4_3001 =  (((rd.dia-10)/2)+20)
        lb5_3001 = math.sqrt((((rd.dia-10)/2)**2)-(980**2))+20
        r_3001 = (rd.dia-10)/2

        le1_3001 = ((rd.dia-10)/2)-960
        #--------------3501 - 3901 ARASI
        lb1_2_3501 = math.sqrt((((rd.dia-10)/2)**2)-(960**2))+20
        lb3_3501 = ((rd.dia-10)/2)+20
        lb4_3501 = math.sqrt((((rd.dia-10)/2)**2)-(980**2))+20
        lb5_3501 = ((rd.dia-10)/2)+20
        lb6_3501 = math.sqrt((((rd.dia-10)/2)**2)-(980**2))+20

        le1_3501 = ((rd.dia-10)/2)-960
        le2_3501 = ((rd.dia-10)/2)-960
        #--------------3901 - 4000 ARASI
        lb1_3901 = math.sqrt((((rd.dia-10)/2)**2)-(1210**2))+20
        lb2_3901 = math.sqrt((((rd.dia-10)/2)**2)-(1210**2))+20
        lb3_3901 = ((rd.dia-10)/2)+20
        lb4_3901 = math.sqrt((((rd.dia-10)/2)**2)-(1230**2))+20
        lb5_3901 = ((rd.dia-10)/2)+20
        lb6_3901 = math.sqrt((((rd.dia-10)/2)**2)-(1230**2))+20

        le1_3901 = ((rd.dia-10)/2)-1210

        #-----------------9

        if rd.ground_circle: kanopi_en = YUVARLA((rd.canopy * 2)+200)
        else: kanopi_en = YUVARLA((rd.canopy * 2) + 100)   

        if rd.night_sensor:
            kanopi_yukseklik = (rd.dia/2)+200
            kanopi_boy = rd.dia+300
        else:
            kanopi_yukseklik = (rd.dia/2)+100
            kanopi_boy = rd.dia+100

        sabit_kanat_en = YUVARLA(((rd.dia-94)/2)-((rd.dia-94)/4)*math.sqrt(3)+240)         
        sabit_kanat_yukseklik = YUVARLA((((rd.dia-94)/2)+80))
        sabit_kanat_boy = YUVARLA((rd.trans_height+45)+50)
        
        hareketli_kanat_en = 300
        hareketli_kanat_yukseklik = YUVARLA((((rd.dia - 244)/2)+50))
        hareketli_kanat_boy = YUVARLA(((rd.dia + 20)/10))

        if rd.night_sensor:
            gece_kalkani_en = YUVARLA(((rd.dia / 2)+ 38)- math.sin((74*3.141593)/180) * ((rd.dia / 2) + 38 ) + 120)
            gece_kalkani_yukseklik = (((rd.dia / 2)+ 38)-30)*3.14/6+50
            gece_kalkani_boy = (rd.trans_height + 20) / 10
            

        #-----------------9.1

        dis_cap_9 = rd.dia - 4
        dis_kesim_u = YUVARLA((((rd.dia - 4)*3.15)/2))
        dis_cap_9_2 = rd.dia - 34
        dis_kesim_u_2 = YUVARLA(((((rd.dia - 34)*3.14)/6)+15)-108) 
        dis_kesim_u_3 =  YUVARLA((((((rd.dia - 34)*3.14)/6)*2)+40))
        dis_cap_9_5 = (rd.dia - 34)- 60 
        dis_kesim_u_5 = YUVARLA(((((rd.dia - 34) - 60)*3.14)/2)+40)

        context = {
            'rd':rd,
            'ph':int(ph),'pr':int(pr),'ch':int(ch),
            'cr':int(cr),'iydograma':int(iydograma),'dydograma':int(dydograma),
            'iycam':int(iycam),'dycam':int(dycam),'ik':int(ik),'dk_3':int(dk_3),'us_dis':int(us_dis),
            'ts_dis_kesim':int(ts_dis_kesim),'ts_dis_cap':int(ts_dis_cap),
            'us_dis_kesim':int(us_dis_kesim),'us_dis_cap':int(us_dis_cap),
            'kanopi_birlesim':int(kanopi_birlesim),'kbu_u_profile':int(kbu_u_profile),'sbu_u_profile':int(sbu_u_profile),
            's1':int(s1),'s2':int(s2),'s3':int(s3),'u_prf_dis_kesim':int(u_prf_dis_kesim),'u_profile_dis_cap':u_profile_dis_cap,
            'k1':int(k1),'dk_4':int(dk_4),'ad':int(ad),'kb':int(kb),'kl':int(kl),'ch_sabit_kanat':int(ch_sabit_kanat),'cl':int(cl),
            'ek':int(ek),'k2':int(k2),'lb':int(lb),'dy':int(dy),'iy':int(iy),'r2':float(r2),
            'lb_2':int(lb_2),'dy_2':int(dy_2),'iy_2':int(iy_2),'r2_2':float(r2_2),'sm':float(sm),
            'lb_3':int(lb_3),'dy_3':int(dy_3),'iy_3':int(iy_3),'r2_3':r2_3,'r_radus_8':int(r_radus_8),'lb':int(lb),'le':int(le),
            'lb_le':lb_le,'le_2':int(le_2),'lb_2':int(lb_2),'lb1_3001':lb1_3001,'lb2_3001':int(lb2_3001),
            'lb3_3001':lb3_3001,'lb4_3001':int(lb4_3001),'lb5_3001':lb5_3001,'r_3001':int(r_3001),
            'le1_3001':int(le1_3001),'lb1_2_3501':lb1_2_3501,'lb3_3501':int(lb3_3501),'lb4_3501':lb4_3501,
            'lb5_3501':int(lb5_3501),'lb6_3501':lb6_3501,'le1_3501':int(le1_3501),'le2_3501':int(le2_3501),
            'lb1_3901':lb1_3901,'lb2_3901':lb2_3901,'lb3_3901':int(lb3_3901),'lb4_3901':lb4_3901,
            'lb5_3901':int(lb5_3901),'lb6_3901':lb6_3901,'le1_3901':int(le1_3901),'total_height':int(total_height),
            'dis_cap_9':dis_cap_9,'dis_kesim_u':dis_kesim_u,'dis_cap_9_2':dis_cap_9_2,'dis_kesim_u_2':dis_kesim_u_2,'dis_kesim_u_3':dis_kesim_u_3,
            'dis_cap_9_5':dis_cap_9_5,'dis_kesim_u_5':dis_kesim_u_5,'kanopi_en':int(kanopi_en),
            'kanopi_yukseklik':int(kanopi_yukseklik),'kanopi_boy':int(kanopi_boy),'sabit_kanat_en':sabit_kanat_en,
            'sabit_kanat_yukseklik':int(sabit_kanat_yukseklik),'sabit_kanat_boy':int(sabit_kanat_boy),
            'hareketli_kanat_boy':int(hareketli_kanat_boy),'hareketli_kanat_en':int(hareketli_kanat_en),'hareketli_kanat_yukseklik':int(hareketli_kanat_yukseklik),
            'gece_kalkani_en':int(gece_kalkani_en),'gece_kalkani_yukseklik':int(gece_kalkani_yukseklik),'gece_kalkani_boy':int(gece_kalkani_boy),
            
        }
    
        return render(request,'revolving_door/detail-revolving-door.html',context)
    else:
        return redirect('401')    