# Generated by Django 4.2.1 on 2023-06-08 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='objeto_inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
