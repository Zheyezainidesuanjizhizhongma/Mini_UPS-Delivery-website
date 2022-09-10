# Generated by Django 4.0.4 on 2022-04-24 03:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ups_front', '0002_auto_20220424_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package_info',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_package', to=settings.AUTH_USER_MODEL),
        ),
    ]