# Generated by Django 2.2.3 on 2020-01-30 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200130_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
