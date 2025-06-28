from django.http import JsonResponse
from .models import Orders

def update_order_status(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        try:
            order = Orders.objects.get(id=data['order_id'])
            order.status = data['status']
            if data['status'] == 4:  # Mark as completed if status is 4
                order.isCompleted = True
            order.save()
            return JsonResponse({"success": True})
        except Orders.DoesNotExist:
            return JsonResponse({"success": False, "error": "Order not found"})
    return JsonResponse({"success": False, "error": "Invalid request method"})
