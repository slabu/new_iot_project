# Generated by Django 3.2.9 on 2021-12-06 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_controler_chart_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controler',
            name='chart_url',
            field=models.URLField(blank=True, default=None),
        ),
    ]