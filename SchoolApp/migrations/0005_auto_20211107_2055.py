# Generated by Django 3.2.9 on 2021-11-07 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0004_auto_20211107_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='id_t',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
