# Generated by Django 4.0 on 2022-01-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_purchase_purchase_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='received_type',
            field=models.CharField(choices=[('Received', 'Received'), ('Not Received Yet', 'Not Received Yet')], default='Received', max_length=50),
        ),
    ]
