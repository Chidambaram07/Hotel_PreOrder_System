import json
from django.shortcuts import render,redirect
from hotelapp import Food_Items, Order_Items
from hotelapp.accounts import LoginUser,RegisterUser
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required,user_passes_test
from hotelapp.updateOrderStatus import update_order_status
# Create your views here.
def is_admin(user):
    return user.is_authenticated and user.is_staff
def index(request):
    n=3
    context={"items":Food_Items.get_top_sellings(n)}
    return render(request,'index.html',context=context)
@user_passes_test(is_admin)
def addItem(request):
    if request.method=='POST':
        status,context=Food_Items.add_item(request)
        return render(request,"addItem.html",context=context)
    return render(request,"addItem.html")
def accounts(request):
    redirect_url=request.GET.get('redirectFrom')
    if request.user.is_authenticated:
        if redirect_url is not None:
            return redirect(redirect_url)
        else:
            return redirect('/')
    if request.method=='POST':
        if request.POST.get('form_type')=="login":
            status,context=LoginUser(request)
            if status:
                print("login successfull")
                if redirect_url is not None:
                    return redirect(redirect_url)
                return redirect('/')
            else:
                context["action"]="login"
                print(context)
                return render(request,"accounts.html",context=context)
        else:
            status,context=RegisterUser(request)
            if status:
                print("register successfull")
                if redirect_url is not None:
                    return redirect(redirect_url)
                return redirect('/')
            else:
                context["action"]="register"
                print(context)
                return render(request,"accounts.html",context=context)
    return render(request,'accounts.html')
def menu(request):
    if(request.method=='POST'):
        Order_Items.proceedToOrder(request)
        if request.user.is_authenticated:
            return redirect('/order')
        else:
            return redirect('/accounts?redirectFrom=/order')
    context={
        "food":Food_Items.get_items()
    }
    return render(request,"menu.html",context=context)
def order(request):
    if request.method=="GET":
        cart_data = request.session.get('cart_items', [])
        total_price = request.session.get('total_price', 0)
        print(cart_data)
        return render(request, 'order.html', {
        'cart_items': cart_data,
        'total_price': total_price
        })
    if request.method=="POST":
        if Order_Items.CreateOrder(request):
            return redirect('/TrackOrder')
    return render(request,"order.html")
def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='accounts',redirect_field_name='redirectFrom')
def ordertrack(request):
    order=Order_Items.GetLatestOrder(request)
    print(order)
    return render(request,'ordertrack.html',{"order":order})
@user_passes_test(is_admin)
def userorders(request):
    orders=Order_Items.GetAllOrders(request)
    return render(request,'userordered.html',{"orders":orders})

#Update order status view
def uos(request):
    return update_order_status(request)