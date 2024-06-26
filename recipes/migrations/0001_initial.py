# Generated by Django 4.2.11 on 2024-04-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cooking_time', models.IntegerField(help_text='minutes')),
                ('ingredients', models.CharField(help_text='Please separate ingredients with a ", "', max_length=255)),
                ('description', models.TextField()),
                ('pic', models.ImageField(default='no-image.jpg', upload_to='recipes')),
            ],
        ),
    ]
