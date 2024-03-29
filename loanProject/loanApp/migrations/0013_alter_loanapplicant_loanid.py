# Generated by Django 4.2.8 on 2023-12-16 18:13

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):
    dependencies = [
        ("loanApp", "0012_alter_loanapplicant_employmenttype_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loanapplicant",
            name="LoanID",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid,
                max_length=12,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
