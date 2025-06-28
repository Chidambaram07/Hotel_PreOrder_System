
import json
from hotelapp.models import FoodItems, Orders


def add_item(request):
    if request.method=='POST' and request.FILES.get('food_img'):
        fname=request.POST.get('food_name')
        des=request.POST.get('description')
        category=request.POST.get('sel_cat')
        meal=request.POST.get('sel_meal')
        image=request.FILES['food_img']
        if image.size > 5 * 1024 * 1024:  # 5MB max size
            return False,{'error': 'Image file too large (max 5MB).'}

        if image.content_type not in ['image/jpeg', 'image/png']:
            return False , {'error': 'Only JPEG and PNG formats are supported.'}
        price=request.POST.get('cost')
        data={
            "Description":des,
            "Category":category,
            "Meal":meal,
            "Price":price,
        }
        new_item=FoodItems(food_name=fname,data=data,image=image)
        new_item.save()
        return True,{"success":"Food Item added successfully!"}
    return False,{"error":"*Something went wrong!"}

def get_items():
    items=FoodItems.objects.filter(isAvailable=True)
    return items

def get_top_sellings(n):
    items=FoodItems.objects.filter(isAvailable=True).order_by('-id')[:n]
    return items
