# Generated by Django 2.2.13 on 2021-02-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagementSystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='status',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='status',
            field=models.CharField(default='active', max_length=100),
        ),
    ]
