# Generated by Django 4.2.2 on 2023-06-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sochapp', '0003_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(upload_to='media/files'),
        ),
    ]