# Generated by Django 4.2.3 on 2024-07-28 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DosageForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage_form', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('active_ingredients', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterationDecree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decree_no', models.IntegerField(default=296)),
                ('year', models.IntegerField(default=2009)),
            ],
        ),
        migrations.CreateModel(
            name='StabilityApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=100)),
                ('physical_character', models.CharField(max_length=400)),
                ('pack', models.CharField(max_length=400)),
                ('study_length', models.CharField(choices=[(3, '3 Months'), (6, '6 Months'), (12, '12 Months'), (18, '18 Months'), (24, '24 Months'), (36, '36 Months')], default=3, max_length=2)),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='RegisterationLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=100)),
                ('active_ingredients', models.CharField(max_length=400)),
                ('physical_character', models.CharField(max_length=400)),
                ('shelf_life', models.CharField(max_length=400)),
                ('storage_condition', models.CharField(max_length=100)),
                ('approved_pack', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=100)),
                ('type_of_license', models.CharField(max_length=100)),
                ('license_holder', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=1000)),
                ('storage_site', models.CharField(max_length=1000)),
                ('manufacturer_of_active_substance', models.CharField(max_length=3000)),
                ('notes', models.TextField()),
                ('issuance_date', models.DateField()),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('registeration_number', models.CharField(max_length=20)),
                ('invalidation_date', models.DateField()),
                ('decree_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.registerationdecree')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='decree_no',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.registerationdecree'),
        ),
        migrations.AddField(
            model_name='product',
            name='dosage_form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.dosageform'),
        ),
        migrations.CreateModel(
            name='NameApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(max_length=1000)),
                ('arabic_name', models.CharField(max_length=1000)),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='LayoutApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateField(null=True)),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='InsertApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_date', models.DateField(null=True)),
                ('revised_by', models.CharField(max_length=100)),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='CompositionApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(null=True)),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ComparativeApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('study_reason', models.CharField(max_length=1000)),
                ('raw_material_supplier_name', models.CharField(max_length=200)),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='CADCApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sic', models.CharField(max_length=100)),
                ('batch_no', models.CharField(max_length=100)),
                ('result', models.CharField(choices=[(True, 'Conform'), (False, 'Not Conform')], default=False, max_length=1)),
                ('issue_date', models.DateField()),
                ('sampling_reason', models.CharField(choices=[(1, 'Pilot'), (2, 'First Three Production Batches'), (3, 'Variation'), (4, 'Random'), (5, 'Other')], default=4, max_length=1)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='BoxApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generic_name_and_strength', models.CharField(max_length=1000)),
                ('company_name', models.CharField(max_length=1000)),
                ('package_information', models.CharField(max_length=1000)),
                ('reference_stated_in_company_application', models.CharField(max_length=1000)),
                ('application_no', models.IntegerField()),
                ('box_request_number', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('attachment', models.FileField(upload_to='', verbose_name='.')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
