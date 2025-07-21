from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from auditlog.registry import auditlog
from django.forms import ValidationError
from django.urls import reverse
from CMS.sharedutils import upload_to

# Your other model definitions
class DosageForm(models.Model):
    dosage_form = models.CharField(max_length=300)
    code = models.CharField(max_length=6)
    def __str__(self):
        return self.dosage_form

class RegisterationDecree(models.Model):
    decree_no = models.IntegerField(default=296)
    year = models.IntegerField(default=2009)
    def __str__(self):
        return str(self.decree_no) + "/" + str(self.year)

class Product(models.Model):
    class Meta:
        ordering = ["name"]
    name = models.CharField(max_length=1000)
    dosage_form = models.ForeignKey(DosageForm, on_delete=models.CASCADE,default=1)
    active_ingredients = models.CharField(max_length=1000)
    decree_no = models.ForeignKey(RegisterationDecree,on_delete=models.CASCADE,default=1)

    def get_absolute_url(self):
        return reverse("index")

    def __str__(self):
        return self.name

class CompositionApproval(models.Model):
    issue_date = models.DateField(null=True)
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(choices=[
        (1,"Active"),
        (0,"Superseded")
    ],default=1,max_length=1)
    def __str__(self):
        return str(self.issue_date)

class BoxApproval(models.Model):
    generic_name_and_strength = models.CharField(max_length=1000)
    company_name = models.CharField(max_length=1000)
    package_information = models.CharField(max_length=1000)
    reference_stated_in_company_application = models.CharField(max_length=1000)
    application_no = models.IntegerField()
    box_request_number = models.IntegerField()
    issue_date = models.DateField()
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("product:detail_boxapproval", kwargs={"pk": self.product.pk,"ba_pk":self.pk})
    

    def __str__(self):
        return self.generic_name_and_strength

class NameApproval(models.Model):
    english_name = models.CharField(max_length=1000)
    arabic_name =  models.CharField(max_length=1000)
    issuance_date = models.DateField(null=True)
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def clean(self) -> None:
        if self.issuance_date > timezone.now().date():
            raise ValidationError("The issuance date can't be in the future")
        return super().clean()

    def get_absolute_url(self):
        return reverse("product:detail_nameapproval", kwargs={"name_approval_pk": self.pk,"pk":self.product.id})
    
    def __str__(self):
        return self.english_name

class StabilityApproval(models.Model):
    batch_no = models.CharField(max_length=100)
    physical_character = models.CharField(max_length=400)
    pack = models.CharField(max_length=400)
    study_length = models.IntegerField(choices=[
        (3,"3 Months"),
        (6,"6 Months"),
        (12,"12 Months"),
        (18,"18 Months"),
        (24,"24 Months"),
        (36,"36 Months"),
    ],default=3)
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.batch_no) + " | " + str(self.study_length)
    
    def get_absolute_url(self):
        return reverse("product:detail_stabilityapproval", kwargs={"sa_pk": self.pk,"pk":self.product.id})

class ComparativeApproval(models.Model):
    batch_no = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    study_reason = models.CharField(max_length=1000)
    raw_material_supplier_name = models.CharField(max_length=200)
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.batch_no

class CADCApproval(models.Model):
    sic = models.CharField(max_length=100)
    batch_no = models.CharField(max_length=100)
    result = models.BooleanField(choices=[
        (True, "Conform"),
        (False, "Not Conform")
    ],default=False,max_length=1)
    issue_date = models.DateField()
    sampling_reason = models.IntegerField(choices=[
        (1,"Pilot"),
        (2,"First Three Production Batches"),
        (3,"Variation"),
        (4,"Random"),
        (5,"Other")
    ],default=4)
    upload_date = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return self.batch_no + " | "  + self.sic

class RegisterationLicense(models.Model):
    trade_name = models.CharField(max_length=100)
    active_ingredients = models.CharField(max_length=400)
    physical_character = models.CharField(max_length=400)
    shelf_life = models.CharField(max_length=400)
    storage_condition = models.CharField(max_length=100)
    approved_pack = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    type_of_license = models.CharField(max_length=100)
    license_holder = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=1000)
    storage_site = models.CharField(max_length=1000)
    manufacturer_of_active_substance = models.CharField(max_length=3000)
    notes = models.TextField(null=True)
    issuance_date = models.DateField()
    attachment = models.FileField(upload_to=upload_to)
    decree_no = models.ForeignKey(RegisterationDecree,on_delete=models.CASCADE)
    registeration_number = models.CharField(max_length=20)
    invalidation_date = models.DateField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


    def clean(self) -> None:
        if self.issuance_date > timezone.now().date():
            raise ValidationError("Issuance Date can't be in the future")
        
        if self.issuance_date > self.invalidation_date:
            raise ValidationError("Issuance Date can't be higher than Invalidation date.")
        return super().clean()

    def __str__(self):
        return str(self.registeration_number) + " | " + str(self.invalidation_date)
    
    def get_absolute_url(self):
        return reverse("product:detail_registerationlicense", kwargs={"rl_pk": self.pk,"pk":self.product.id})

class InsertApproval(models.Model):
    approval_date = models.DateField(null=True)
    revised_by = models.CharField(max_length=100)
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class PriceApproval(models.Model):
    price = models.FloatField()
    unit = models.CharField(max_length=100)
    issuance_no = models.IntegerField()
    issuance_date = models.DateField()
    attachment = models.FileField(upload_to=upload_to)
    notes = models.TextField(null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

class LayoutApproval(models.Model):
    approval_date = models.DateField(null=True)
    attachment = models.FileField(upload_to=upload_to)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

auditlog.register(RegisterationLicense)
auditlog.register(ComparativeApproval)
auditlog.register(RegisterationDecree)
auditlog.register(CompositionApproval)
auditlog.register(StabilityApproval)
auditlog.register(InsertApproval)
auditlog.register(LayoutApproval)
auditlog.register(PriceApproval)
auditlog.register(CADCApproval)
auditlog.register(NameApproval)
auditlog.register(BoxApproval)
auditlog.register(DosageForm)
auditlog.register(Product)
auditlog.register(User)