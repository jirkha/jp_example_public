# Generated by Django 4.1 on 2022-10-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_discount_transaction_difference_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='real_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
