"""appcatering URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from menu import views as menuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',menuView.home,name='home'),
    path('makanan/<int:makanan_id>',menuView.detail,name='detail'),
    path('minuman/',menuView.minuman,name='minuman'),
    path('minuman/<int:minuman_id>',menuView.detail_minuman,name='detail_minuman'),
    path('cart/',menuView.view_cart,name='cart'),
    path('add_to_cart/<int:makanan_id>/',menuView.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:makanan_id>/',menuView.remove_from_cart,name='remove_from_cart'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)