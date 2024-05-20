# Generated by Django 4.2.11 on 2024-05-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.FloatField(help_text='minutes'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=350),
        ),
    ]
