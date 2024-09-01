from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class RegisterationLicenseResource(resources.ModelResource):

    class Meta:
        model = RegisterationLicense

class RegisterationLicenseAdmin(ImportExportModelAdmin):
    resource_classes = [RegisterationLicenseResource]

class ComparativeApprovalResource(resources.ModelResource):

    class Meta:
        model = ComparativeApproval

class ComparativeApprovalAdmin(ImportExportModelAdmin):
    resource_classes = [ComparativeApprovalResource]

admin.site.register(RegisterationLicense,RegisterationLicenseAdmin)
admin.site.register(ComparativeApproval,ComparativeApprovalAdmin)
admin.site.register(RegisterationDecree)
admin.site.register(CompositionApproval)
admin.site.register(StabilityApproval)
admin.site.register(InsertApproval)
admin.site.register(LayoutApproval)
admin.site.register(PriceApproval)
admin.site.register(CADCApproval)
admin.site.register(NameApproval)
admin.site.register(BoxApproval)
admin.site.register(DosageForm)
admin.site.register(Product)