from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *

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
        self.fields["product"].widget.attrs.update({'disabled': ''})

    class Meta:
        model = NameApproval
        fields = "__all__"


