from fkartapp import views
from django.urls import path
from fkartapp.views import ContactForm
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('about',views.about),
    path('contact',views.contact),
    path('products',views.products),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('filterbyprice',views.filterbyprice),
    path('product_details/<pid>',views.product_detail),
    path('addcart/<pid>',views.cart),
    path('viewcart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('removecart/<cid>',views.removecart),
    path('removefetchordercart/<cid>',views.removefetchordercart),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.paymentsuccess),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)