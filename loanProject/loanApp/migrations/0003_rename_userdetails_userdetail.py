# Generated by Django 4.2.7 on 2023-12-07 19:20

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("loanApp", "0002_rename_user_userdetails"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UserDetails",
            new_name="UserDetail",
        ),
    ]
