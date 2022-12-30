"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('add/',views.add_to_cart, name='add'),
    path('addon/',views.add_cart, name='addon'),
    path('cart/',views.cart, name='cart'),
    path('transaction', views.transactionview, name='transaction'),
    path('detail_transaction/<tran>', views.detail_transaction, name='detail_transaction'),

    path('qr_mobile/<mobile>/<amount>/qr.png', views.get_qr, name='qr'),
    path('qr_nid/<nid>/<amount>/', views.get_qr, name='qr'),
    path('ct', views.createTransaction, name='ct'),
    path('removeon/',views.remove_cart, name='removeon'),
    path('detail/<str:pk>/', views.product_detail, name='photo')
]


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
