# Generated by Django 4.1.6 on 2023-02-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]