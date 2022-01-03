# Generated by Django 4.0 on 2022-01-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0006_alter_purchase_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='tax_type',
            field=models.CharField(choices=[('Exclusive', 'Exclusive'), ('Inclusive', 'Inclusive')], default='Exclusive', max_length=50),
        ),
    ]
