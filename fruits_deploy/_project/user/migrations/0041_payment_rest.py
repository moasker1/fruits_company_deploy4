# Generated by Django 3.2.23 on 2024-01-08 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_remove_payment_rest'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='rest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
    ]
