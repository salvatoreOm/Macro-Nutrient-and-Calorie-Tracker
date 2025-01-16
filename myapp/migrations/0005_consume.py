# Generated by Django 5.1.4 on 2025-01-15 11:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_caloiresburnt_caloriesburnt'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie_burnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.caloriesburnt')),
                ('food_consumed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.food')),
                ('supplement_consumed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.supplements')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]