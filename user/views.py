from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,UpdateMR30Form,DeleteFORM
from django.contrib.auth.models import User
from services.models import RevolvingDoor

def login_view(request):
    if request.user.is_authenticated == False:
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        return render(request, "user/loginform.html", {"form": form,'title':'Giriş Yap',})
    else:
        return redirect('home')


def logout_view(request):

    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('401')


def history_view(request):
    if request.user.is_authenticated:

        context = {}
        return render(request,'user/history.html',context)
    
    else:
        return redirect('401') 


def mr30_history_view(request):

    if request.user.is_authenticated:


        user1 = User.objects.get(id=request.user.id)
        user1_data = user1.revolvingdoor_set.all()

        context= {
            'user1_data':user1_data,
        }

        return render(request,'user/islemler/mr30-history.html',context)
    else:
        return redirect('401')    



def mr30_detail_view(request):

    if request.user.is_authenticated:


        user1 = User.objects.get(id=request.user.id)
        user1_data = user1.revolvingdoor_set.all()

        context= {
            'user1_data':user1_data,
        }

        return render(request,'user/islemler/mr30-update.html',context)
    else:
        return redirect('401')          



def mr30_update_views(request,id):

    if request.user.is_authenticated:

        data = get_object_or_404(RevolvingDoor,id=id)
        form = UpdateMR30Form(request.POST or None,instance=data)
        ral_error = False
        if form.is_valid():
            color = form.cleaned_data.get('color')
            ral_color_code = form.cleaned_data.get('ral_color_code')
            if color == 'Ral Boya':
                if ral_color_code:

                    update_post = form.save()
                    return redirect('history')
                else:
                    ral_error = True
            else:
                update_post = form.save()
                return redirect('history')

                
        context = {
            'form':form,
            'id':id,
            'ral_error':ral_error,
        }
        return render(request,'user/islemler/mr30-update.html',context)

    else:
        return redirect('401')    


def mr30_delete_views(request,id):

    if request.user.is_authenticated:
        data = RevolvingDoor.objects.get(id=id)

        form = DeleteFORM(request.POST or None)
        
        if form.is_valid():

            data.delete()
            return redirect('mr30_history')

        context = {
            'id':id,
            'form':form,
            'data':data,
        }
        
        return render(request,'user/islemler/mr30-delete.html',context)
