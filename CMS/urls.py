from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView
from products.views import cve_log
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "CMS"

urlpatterns = [
    path('',TemplateView.as_view(template_name="./main/index.html"),name="index"),
    path('cve/', cve_log, name="list_cve"),
    path('admin/', admin.site.urls),
    path('login/', CustomLoginview.as_view(),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),
    path('products/',include("products.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    
