# Generated by Django 3.1.5 on 2021-01-12 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210112_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.speciality'),
        ),
    ]