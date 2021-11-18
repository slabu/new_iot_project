# Generated by Django 3.2.9 on 2021-11-18 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cheese_condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_condition', models.TextField(max_length=300)),
                ('previous_condition', models.CharField(max_length=30)),
                ('term_days', models.IntegerField()),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.cheese')),
            ],
        ),
    ]