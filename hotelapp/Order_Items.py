
from datetime import datetime
from hotelapp.models import Orders


def proceedToOrder(request):
    if request.method == "POST":
        cart_items = []
        index = 0
        while True:
            food_name = request.POST.get(f'cart_items[{index}][food_name]')
            quantity = request.POST.get(f'cart_items[{index}][quantity]')
            price = request.POST.get(f'cart_items[{index}][price]')

            if not food_name:  # Exit when no more items are found
                break

            cart_items.append({
                'food_name': food_name,
                'quantity': int(quantity),
                'price': float(price),
            })
            index += 1
        print(cart_items)
        total_price = request.POST.get('total_price', 0)
        request.session['cart_items']=cart_items
        request.session['total_price']=total_price
        return True
def CreateOrder(request):
    if request.method=="POST":
        pickup=request.POST.get('pickup-time')
        pickup_time = datetime.strptime(pickup, '%H:%M').time()
        instructions=request.POST.get('instructions')
        food=request.session.get('cart_items',[])
        total_cost=request.session.get('total_price',0)
        customer=request.session.get('user')
        print(customer)
        order=Orders(Food=food,Customer=request.user,cost=total_cost,instruction=instructions,pick_up_time=pickup_time)
        order.save()
        del request.session['cart_items']
        del request.session['total_price']
        return True
    return False
def GetAllOrders(request):
    food_orders=Orders.objects.filter(isCompleted=False).order_by('-id')
    return food_orders

def GetLatestOrder(request):
    order=Orders.objects.filter(Customer=request.user,isCompleted=False).order_by('-id')
    return order