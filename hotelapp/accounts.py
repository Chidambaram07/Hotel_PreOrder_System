from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login

from hotelapp.models import UserDetails
def LoginUser(request):
    action=request.POST.get('form_type')
    if action=='login':
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        print(email,password)
        try:
            cu_user=User.objects.get(email=email)
            if cu_user is not None:
                username=cu_user.username
        except:
            return False,{"error":"* No email registered with this account!"}
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            #customer=UserDetails.objects.get(Customer=user)
            #request.session['user']=customer
            login(request,user)
            return True,{}
        else:
            return False,{"error":"* Incorrect password!"}
    return False,{"error":"* Something went wrong!"}

def RegisterUser(request):
    email=request.POST.get("email")
    username=request.POST.get("username")
    password=request.POST.get("pwd")
    con_password=request.POST.get("con_pwd")
    mobile=request.POST.get("mobile")
    if(password!=con_password):
        return False,{"error":"* Passwords don't match!"}
    if(User.objects.filter(email=email).exists()):
        return False,{"error":"* Email already registered! Try logging in!"}
    if(User.objects.filter(username=username).exists()):
        return False,{"error":"* Username has already been taken!"}
    if(UserDetails.objects.filter(mobile=mobile).exists()):
        return False,{"error":"*This mobile number is already registered!"}
    user=User.objects.create_user(username=username,password=password,email=email)
    customer=UserDetails(Customer=user,mobile=mobile)
    customer.save()
    #request.session['user']=customer
    login(request,user)
    return True,{"error":""}