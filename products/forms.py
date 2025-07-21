from typing import Any, Mapping
from django import forms
from .models import *

class ProductForm():
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.formname = "Product"
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = Product
        fields = "__all__"

class BaseMeta:
    fields = "__all__"
    exclude = ["product"]

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Automatically assign DateInput to any field ending with 'date'
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
        
class CustomForm(BaseModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formname = self.Meta.model.__name__  # Set form name dynamically from model name

    class Meta(BaseMeta):
        model = None  # This will be overridden in child classes
        widgets = {}

class RegisterationLicenseForm(CustomForm):
    class Meta(CustomForm.Meta):
        model = RegisterationLicense
        widgets = {
            "issuance_date":forms.DateInput(attrs={'type':'date'}),
            "invalidation_date":forms.DateInput(attrs={'type':'date'}),
        }

class NameApprovalForm(CustomForm):
    class Meta(CustomForm.Meta):
        model = NameApproval
        widgets = {
            "issuance_date":forms.DateInput(attrs={'type':'date'}),
        }

class BoxApprovalForm(CustomForm):
    class Meta(CustomForm.Meta):
        model = BoxApproval
        widgets = {
            "issue_date":forms.DateInput(attrs={'type':'date'}),
        }

class StabilityApprovalForm(CustomForm):
    class Meta(CustomForm.Meta):
        model = StabilityApproval

class ComparativeApprovalForm(CustomForm):

    class Meta(CustomForm.Meta):
        model = ComparativeApproval

class CADCApprovalForm(CustomForm):
    class Meta(CustomForm.Meta):
        #make sure Issue Date is a date input
        widgets = {
            "issue_date":forms.DateInput(attrs={'type':'date'}),
        }
        model = CADCApproval

class PriceApprovalForm(CustomForm):
    class Meta(CustomForm.Meta):
        model = PriceApproval

class InsertApprovalForm(CustomForm):
    class Meta(CustomForm.Meta):
        model = InsertApproval

class LayoutApprovalForm(CustomForm):
    class Meta(CustomForm.Meta):
        model = LayoutApproval