# Generated by Django 4.2.1 on 2023-06-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sochapp", "0004_memberposition_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="members",
            name="full_name",
            field=models.CharField(default="", max_length=1000),
        ),
    ]
