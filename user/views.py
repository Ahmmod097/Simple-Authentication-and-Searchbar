from django.shortcuts import render, redirect 
from django.http import HttpResponse, JsonResponse
from .forms import UserRegisterForm, ChangePassword 
from .models import UserInfo
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages

import json
from datetime import datetime


def userRegister(request):
    form = UserRegisterForm()
    if request.is_ajax():
        form = UserRegisterForm(request.POST)
        
       
        
        if form.is_valid():
            print("Hello")
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            address = request.POST['address']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            birthdate = request.POST['birthdate']

            time = datetime.now().date()
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
            
            time = (time - birthdate)
            s1 = time.days
            age = s1//365

            u_name = email
            password = request.POST['password2']

            obj1 = User.objects.all()
            li1=[]
            flag = 0
            for i in obj1:
                li1.append(i.email)
                if(i.email != email):
                    flag+=1
                   
            if(flag==len(li1)):
                userInfo = UserInfo.objects.create(
                                        first_name = first_name,
                                        last_name = last_name,
                                        address = address,
                                        phone = phone_number,
                                        email = email,
                                        age = age,
                                        username = u_name
                                        )
                userInfo.save()
                p_hash = make_password(password)
                my_user = User.objects.create(
                        username = u_name,
                        email = email,
                        password = p_hash)
                
                my_user.save()
                return JsonResponse({
                    'message': 'success'
                    })
            else:
                
                return JsonResponse({
                    'message': 'taken'
                    })
            

        else:
            form = UserRegisterForm()
        
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    
    context1 = request.user
    context2 = ""
    obj2 = ""
    obj3=""
    obj4=""
    obj5=""
    obj6=""
    obj7 = ""
    obj8=""
    temp=0
    if(context1.is_superuser):
        temp=1
        c1 = User.objects.all()
        for i in c1:
            if i==context1:
                context2 = i.username
                break
        
    else:
          
        obj1 = UserInfo.objects.all()
        obj2 = ""
        obj3=""
        obj4=""
        obj5=""
        obj6=""
        obj7 = ""
        obj8=""
        for i in obj1:
            if i.email==context1.email:
                obj2 = i.first_name + i.last_name
                obj3 = i.first_name
                obj4 = i.last_name
                obj5 = i.address
                obj6 = i.phone
                obj7 = i.email
                obj8 = i.age 
                break 
        
        context2 = obj2
    print(context2)
    return render(request, 'user/profile.html',{'context':context2, 'context1':temp,
                                                'context2':obj3,'context3':obj4,
                                                'context4':obj5, 'context5':obj6,
                                                'context6':obj7, 'context7':obj8})    
@login_required
def change_Pass(request):

    form = ChangePassword()
    if request.is_ajax():
        form = ChangePassword(request.POST)
        
       
        
        if form.is_valid():
           
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            repass =  request.POST['reenter_password']
            
            if((old_password != new_password )and(new_password==repass)):
                p_hash = make_password(repass)
                c_user = request.user
                obj1 = User.objects.all()
                for i in obj1:
                    if(i.email==c_user.email):
                        i.password = p_hash
                        i.save()
                        break
               
                return JsonResponse({
                    'message': 'success'
                    })
            else:
                
                return JsonResponse({
                    'message': 'fail'
                    })
            

        else:
            form = ChangePassword()
        
    return render(request, 'user/changePassword.html', {'form': form})

@login_required
def adminView(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            search_str = json.loads(request.body).get('searchText')
            result = UserInfo.objects.filter(first_name__icontains=search_str)| UserInfo.objects.filter(last_name__icontains=search_str) | UserInfo.objects.filter(age__istartswith=search_str)| UserInfo.objects.filter(phone__istartswith=search_str) | UserInfo.objects.filter(email__icontains=search_str)
               
            data = result.values()
            return JsonResponse(list(data), safe = False)

        c3 = request.user
        c2 = ""
        c1 = User.objects.all()
        for i in c1:
            if i==c3:
                c2 = i.username
                break

        obj1 = UserInfo.objects.all()
        name=[]
        age = []
        email = []
        phone_number = []
        for i in obj1:
            name.append(i.first_name + " "+ i.last_name)
            age.append(i.age)
            
            email.append(i.email)
            phone_number.append(i.phone)

        return render(request, 'user/adminView.html', {'context':c2, 'context1':name,
                                                        'context2':age,
                                                        'context3':email,
                                                        'context4':phone_number})

    else:
        return render(request, 'user/notadminView.html')                                                    

