from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from .forms import ProductForm
from .models import Product
from django.db.models import Q
# Create your views here.

class DetailProduct(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "./product/detail_product.html"

    def get_object(self):
        pk = self.kwargs["pk"]
        product = {}
        product["basic_data"] = Product.objects.get(pk=pk)
        return product

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




