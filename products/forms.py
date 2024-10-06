from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *

class RegisterationLicenseForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.formname = "Registeration License"
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
    class Meta:
        model = RegisterationLicense
        fields = "__all__"
        exclude = ["product"]
        widgets = {
            'invalidation_date': forms.DateInput(attrs={'type': 'date'}),
            'issuance_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ProductForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.formname = "Product"
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = Product
        fields = "__all__"


class NameApprovalForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.formname = "Name Approval"
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = NameApproval
        exclude = ["product"]
        widgets = {
            "issuance_date":forms.DateInput(attrs={'type':'date'}),
        }

class BoxApprovalForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.formname = "Box Approval"    
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = BoxApproval
        fields = "__all__"
        exclude = ["product"]
        widgets = {
            "issue_date":forms.DateInput(attrs={'type':'date'}),
        }


