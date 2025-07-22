from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView,ListView,DetailView
from .forms import *
from .models import *
from django.db.models import Q
# Create your views here.

class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = "./product/create_product.html"

class CreateRegisterationLicense(CreateView):
    form_class = RegisterationLicenseForm
    template_name = "./product/create_product.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)

class ListRegisterationLicense(ListView):
    model = RegisterationLicense
    context_object_name = "registeration_licenses"
    paginate_by = 200
    template_name = "./product/registeration_license/index.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return NameApproval.objects.filter(
                Q(english_name__icontains=query) |
                Q(arabic_name__icontains=query) |
                Q(issuance_date__icontains=query)
            )
        else:
            return RegisterationLicense.objects.filter(product__pk=self.kwargs["pk"])

class DetailRegisterationLicense(DetailView):
    model = RegisterationLicense
    template_name = "./product/registeration_license/detail.html"
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        pk = self.kwargs.get("rl_pk")
        try:
            return RegisterationLicense.objects.get(pk=pk)
        except RegisterationLicense.DoesNotExist:
            raise Http404("Registeration license doesn't exist.")

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
                Q(application_no__icontains=query) |
                Q(box_request_number__icontains=query)
            )
        else:
            return BoxApproval.objects.filter(product__pk=self.kwargs["pk"])

class DetailBoxApproval(DetailView):
    model = BoxApproval
    template_name = "./product/box_approval/detail.html"
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:

        pk = self.kwargs.get("ba_pk")
        try:
            return BoxApproval.objects.get(pk=pk)
        except NameApproval.DoesNotExist:
            raise Http404("Name Approval doesn't exist.")

class CreateBoxApproval(CreateView):
    form_class = BoxApprovalForm
    template_name = "./product/create_product.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)

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

class DetailNameApproval(DetailView):
    template_name = "./product/name_approval/detail.html"
    model = NameApproval

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        pk = self.kwargs.get("name_approval_pk")
        try:
            return NameApproval.objects.get(pk=pk)
        except NameApproval.DoesNotExist:
            raise Http404("Name Approval doesn't exist.")

class CreateNameApproval(CreateView):
    form_class = NameApprovalForm
    template_name = "./product/create_product.html"
    model = NameApproval

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)


class CreateStabilityApproval(CreateView):
    form_class = StabilityApprovalForm
    template_name = "./product/create_product.html"
    model = StabilityApproval

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)

class DetailStabilityApproval(DetailView):
    template_name = "./product/stability_approval/details.html"
    model = StabilityApproval

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        pk = self.kwargs.get("sa_pk")
        try:
            return StabilityApproval.objects.get(pk=pk)
        except StabilityApproval.DoesNotExist:
            raise Http404("Stability Approval doesn't exist.")
    
class ListStabilityApproval(ListView):
    model = StabilityApproval
    context_object_name = "stability_approvals"
    paginate_by = 200
    template_name = "./product/stability_approval/index.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return StabilityApproval.objects.filter(
                Q(batch_no__icontains=query) |
                Q(study_length__icontains=query)
            )
        else:
            return StabilityApproval.objects.filter(product__pk=self.kwargs["pk"])
        
class CreateComparativeApproval(CreateView):
    form_class = ComparativeApprovalForm
    template_name = "./product/create_product.html"
    model = ComparativeApproval
    def get_absolute_url(self):
        return f"/products/{self.object.product.pk}"
    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)

class DetailComparativeApproval(DetailView):
    template_name = "./product/comparative_approval/details.html"
    model = ComparativeApproval
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        pk = self.kwargs.get("sa_pk")
        try:
            return ComparativeApproval.objects.get(pk=pk)
        except ComparativeApproval.DoesNotExist:
            raise Http404("Stability Approval doesn't exist.")
    
class ListComparativeApproval(ListView):
    model = ComparativeApproval
    context_object_name = "comparative_approvals"
    paginate_by = 200
    template_name = "./product/comparative_approval/index.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return ComparativeApproval.objects.filter(
                Q(english_name__icontains=query) |
                Q(arabic_name__icontains=query) |
                Q(issuance_date__icontains=query)
            )
        else:
            return ComparativeApproval.objects.filter(product__pk=self.kwargs["pk"])


class CreateCADCApproval(CreateView):
    form_class = CADCApprovalForm
    template_name = "./Product/create_product.html"
    model = CADCApproval
    def get_success_url(self):
        return f"/products/{self.object.product.pk}/cadcApproval/{self.object.pk}"
    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        form.instance.product = product
        return super().form_valid(form)

class DetailCADCApproval(DetailView):
    template_name = "./product/cadc_approval/detail.html"
    model = CADCApproval
    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        pk = self.kwargs.get("ca_pk")
        try:
            return CADCApproval.objects.get(pk=pk)
        except CADCApproval.DoesNotExist:
            raise Http404("CADC Approval doesn't exist.")

class ListCADCApproval(ListView):
    model = CADCApproval
    context_object_name = "cadc_approvals"
    paginate_by = 200
    template_name = "./product/cadc_approval/index.html"
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return ComparativeApproval.objects.filter(
                Q(batch_no__icontains=query) |
                Q(sic__icontains=query) |
                Q(sampling_reason__icontains=query)
            )
        else:
            return CADCApproval.objects.filter(product__pk=self.kwargs["pk"])

