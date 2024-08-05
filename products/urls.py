from django.urls import path
from .views import CreateProduct,ListProducts,DetailProduct

app_name = "product"

urlpatterns = [
    path('',ListProducts.as_view(),name="products_index"),
    path('<pk>',DetailProduct.as_view(),name="detail_product"),
    path('create/', CreateProduct.as_view(),name="create_product")
]