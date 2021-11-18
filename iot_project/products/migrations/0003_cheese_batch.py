# Generated by Django 3.2.9 on 2021-11-18 20:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0008_alter_controler_record_datetime'),
        ('products', '0002_cheese_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese_batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('chamber_zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.ripening_chamber_zone')),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cheese')),
            ],
        ),
    ]