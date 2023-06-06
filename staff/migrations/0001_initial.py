# Generated by Django 4.1.1 on 2023-06-06 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=254, verbose_name="название подразделения"
                    ),
                ),
            ],
            options={
                "verbose_name": "подразделение",
                "verbose_name_plural": "подразделения",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=50, verbose_name="название должности"),
                ),
            ],
            options={
                "verbose_name": "должность",
                "verbose_name_plural": "должности",
            },
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lname", models.CharField(max_length=50, verbose_name="фамилия")),
                ("fname", models.CharField(max_length=50, verbose_name="имя")),
                (
                    "sname",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="отчество"
                    ),
                ),
                (
                    "salary",
                    models.DecimalField(
                        blank=True,
                        decimal_places=0,
                        max_digits=14,
                        null=True,
                        verbose_name="оклад",
                    ),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True, upload_to="staff/images", verbose_name="фото"
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата рождения"
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="staff.department",
                        verbose_name="подразделение",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="staff.post",
                        verbose_name="должность",
                    ),
                ),
            ],
            options={
                "verbose_name": "сотрудник",
                "verbose_name_plural": "сотрудники",
                "ordering": ("lname", "fname", "sname"),
            },
        ),
        migrations.AddField(
            model_name="department",
            name="director",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="staff",
                to="staff.staff",
                verbose_name="директор",
            ),
        ),
    ]
