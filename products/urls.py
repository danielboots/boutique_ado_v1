from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
=======
    path("", views.all_products, name="products"),
    path("<product_id>", views.product_detail, name="product_detail"),
]
>>>>>>> 44ff4fb7513d611ee2e83802ff77d9503708f35c
