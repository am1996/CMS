from django.urls import path
from .views import *

app_name = "product"

urlpatterns = [
    path('',ListProducts.as_view(),name="products_index"),
    path('<pk>',DetailProduct.as_view(),name="detail_product"),
    path('<pk>/nameapprovals',ListNameApproval.as_view(),name="list_nameapproval"),
    path('<pk>/nameapprovals/add',CreateNameApproval.as_view(),name="create_nameapproval"),
    path('<pk>/nameapprovals/<name_approval_pk>',DetailNameApproval.as_view(),name="detail_nameapproval"),
    path('<pk>/boxapprovals',ListBoxApproval.as_view(),name="list_boxapproval"),
    path('<pk>/boxapprovals/add',CreateBoxApproval.as_view(),name="create_boxapproval"),
    path('<pk>/boxapprovals/<ba_pk>',DetailBoxApproval.as_view(),name="detail_boxapproval"),
    path('<pk>/registerationlicense/create',CreateRegisterationLicense.as_view(),name="create_registerationlicense"),
    path('<pk>/registerationlicense/<rl_pk>',DetailRegisterationLicense.as_view(),name="detail_registerationlicense"),
    path('create/', CreateProduct.as_view(),name="create_product")
]