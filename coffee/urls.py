from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('search/', views.search, name='search'),
    path('add-to-cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('delete-cart-item/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('about/', views.about, name='about'),
    path('information/', views.information, name='information'),
]


