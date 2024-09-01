from django.views.generic import CreateView,ListView,DetailView
from .forms import *
from .models import *
from django.db.models import Q
# Create your views here.

class DetailProduct(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "./product/detail_product.html"

    def get_object(self):
        pk = self.kwargs["pk"]
        product= Product.objects.prefetch_related().get(pk=pk)
        return product


class ListBoxApproval(ListView):
    model = BoxApproval
    context_object_name = "box_approvals"
    paginate_by = 200
    template_name = "./product/box_approval/index.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return BoxApproval.objects.filter(
                Q(english_name__icontains=query) |
                Q(arabic_name__icontains=query) |
                Q(issuance_date__icontains=query)
            )
        else:
            return BoxApproval.objects.filter(product__pk=self.kwargs["pk"])

class ListNameApproval(ListView):
    model = NameApproval
    context_object_name = "name_approvals"
    paginate_by = 200
    template_name = "./product/name_approval/index.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return NameApproval.objects.filter(
                Q(english_name__icontains=query) |
                Q(arabic_name__icontains=query) |
                Q(issuance_date__icontains=query)
            )
        else:
            return NameApproval.objects.filter(product__pk=self.kwargs["pk"])

class ListProducts(ListView):
    model = Product
    paginate_by = 200
    template_name = "./product/index.html"
    context_object_name = "products"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(
                Q(name__icontains=query) |
                Q(active_ingredients__icontains=query) |
                Q(decree_no__decree_no__icontains=query) | 
                Q(dosage_form__dosage_form__icontains=query)
            )
        else:
            return Product.objects.all()


class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = "./product/create_product.html"

class CreateNameApproval(CreateView):
    form_class = NameApprovalForm
    template_name = "./product/create_product.html"

    def get_initial(self):
        initial = super().get_initial()
        pk = self.kwargs.get("pk")
        initial["product"] = pk
        return initial


