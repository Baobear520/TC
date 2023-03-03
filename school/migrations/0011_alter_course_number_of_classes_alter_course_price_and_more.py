# Generated by Django 4.1.2 on 2023-03-03 08:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0010_alter_enrollment_lessons_alter_enrollment_money_paid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="number_of_classes",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="price",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=7,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="tuition fee",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="lessons",
            field=models.IntegerField(
                blank=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Number of lessons left",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="money_paid",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=7,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Payment",
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="school.student"
            ),
        ),
    ]