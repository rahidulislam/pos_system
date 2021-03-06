# Generated by Django 4.0 on 2021-12-28 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Product Name')),
                ('slug', models.SlugField(unique=True)),
                ('code', models.CharField(max_length=50, verbose_name='Product Code')),
                ('type', models.CharField(choices=[('Standard', 'Standard'), ('Digital', 'Digital'), ('Service', 'Service')], default='Standard', max_length=20, verbose_name='Product Type')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('tax_method', models.CharField(choices=[('Exclusive', 'Exclusive'), ('Inclusive', 'Inclusive')], default='Exclusive', max_length=20, verbose_name='Tax Method')),
                ('description', models.TextField(blank=True, verbose_name='Product Description')),
                ('image', models.ImageField(blank=True, upload_to='product/')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category', to='product.category')),
            ],
        ),
    ]
