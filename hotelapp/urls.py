from django.urls import path
from hotelapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="home"),
    path('home/',views.index,name="home"),
    path('accounts/',views.accounts,name="accounts"),
    path('addItem/',views.addItem,name="addItem"),
    path('menu/',views.menu,name="menu"),
    path('order/',views.order,name="order"),
    path('logout/',views.logoutUser,name="logout"),
    path('TrackOrder/',views.ordertrack,name="trackOrder"),
    path('ViewOrders/',views.userorders,name="viewOrders"),
    path('update-order-status/', views.uos, name='update_order_status'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)