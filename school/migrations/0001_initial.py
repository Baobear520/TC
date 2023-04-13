# Generated by Django 4.1.2 on 2023-04-12 09:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.TextField(max_length=255)),
                (
                    "description",
                    models.TextField(blank=True, max_length=611, null=True),
                ),
                (
                    "number_of_classes",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=7,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="tuition fee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Level",
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
                ("title", models.TextField(max_length=255)),
                (
                    "description",
                    models.TextField(blank=True, max_length=611, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("date_registered", models.DateField(auto_created=True)),
                ("date_of_birth", models.DateField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images",
                        verbose_name="Upload photo",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["user"],},
        ),
        migrations.CreateModel(
            name="Enrollment",
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
                ("date_enrolled", models.DateField(default=django.utils.timezone.now)),
                (
                    "money_paid",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=7,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Payment",
                    ),
                ),
                (
                    "lessons",
                    models.PositiveIntegerField(
                        blank=True, verbose_name="Number of lessons left"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="school.course"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="school.student"
                    ),
                ),
            ],
            options={"ordering": ("date_enrolled",),},
        ),
        migrations.AddField(
            model_name="course",
            name="level",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="school.level"
            ),
        ),
    ]
