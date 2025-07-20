from django.urls import path
from .views import *

app_name = "product"

urlpatterns = [
    
    path('',ListProducts.as_view(),name="products_index"),
    path('<pk>',DetailProduct.as_view(),name="detail_product"),
    path('<pk>/nameapprovals',ListNameApproval.as_view(),name="list_nameapproval"),
    path('<pk>/nameapprovals/create',CreateNameApproval.as_view(),name="create_nameapproval"),
    path('<pk>/nameapprovals/<name_approval_pk>',DetailNameApproval.as_view(),name="detail_nameapproval"),
    path('<pk>/boxapprovals',ListBoxApproval.as_view(),name="list_boxapproval"),
    path('<pk>/boxapprovals/create',CreateBoxApproval.as_view(),name="create_boxapproval"),
    path('<pk>/boxapprovals/<ba_pk>',DetailBoxApproval.as_view(),name="detail_boxapproval"),
    path('<pk>/registerationlicense/create',CreateRegisterationLicense.as_view(),name="create_registerationlicense"),
    path('<pk>/registerationlicense/<rl_pk>',DetailRegisterationLicense.as_view(),name="detail_registerationlicense"),
    path('<pk>/stabilityApproval/create',CreateStabilityApproval.as_view(),name="create_stabilityapproval"),
    path('<pk>/stabilityApproval/<sa_pk>',DetailStabilityApproval.as_view(),name="detail_stabilityapproval"),
    path('<pk>/stabilityApproval/',ListStabilityApproval.as_view(),name="list_stabilityapproval"),
    path('<pk>/comparativeApproval/create',CreateComparativeApproval.as_view(),name="create_comparativeapproval"),
    path('<pk>/comparativeApproval/<ca_pk>',DetailComparativeApproval.as_view(),name="detail_comparativeapproval"),
    path('<pk>/comparativeApproval/',ListComparativeApproval.as_view(),name="list_comparativeapproval"),
    path('<pk>/cadcApproval/create',CreateCADCApproval.as_view(),name="create_cadcApproval"),
    path('<pk>/cadcApproval/<ca_pk>',DetailCADCApproval.as_view(),name="detail_cadcApproval"),
    path('<pk>/cadcApproval/',ListCADCApproval.as_view(),name="list_cadcApproval"),
    path('create/', CreateProduct.as_view(),name="create_product"),
    
]