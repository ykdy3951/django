"""kcw_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from kuser.views import index, RegisterView, LoginView, Logout
from product.views import ProductList, ProductCreate, ProductDetail, ProductListAPI, ProductDetailAPI
from order.views import OrderCreate, OrderList
from board.views import BoardList, BoardWrite, BoardDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # class의 경우 as_view()의 method를 사용해야함
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', Logout),
    path('product/', ProductList.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('order/', OrderList.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('board/', BoardList.as_view()),
    path('board/write/', BoardWrite.as_view()),
    path('board/<int:pk>/', BoardDetail.as_view()),
    path('api/product', ProductListAPI.as_view()),
    path('api/product/<int:pk>/', ProductDetailAPI.as_view()),
]
