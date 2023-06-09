# Generated by Django 4.1.2 on 2023-05-25 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("school", "0002_alter_student_options_remove_student_date_registered"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="grade",
            field=models.CharField(
                choices=[("a", "a"), ("b", "b"), ("c", "c")], default=None, max_length=2
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="level",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="available_courses",
                to="school.level",
            ),
        ),
        migrations.AlterField(
            model_name="course",
            name="title",
            field=models.CharField(
                choices=[
                    ("S1", "Starter 1"),
                    ("S2", "Starter 2"),
                    ("S3", "Starter 3"),
                    ("E1", "Elementary 1"),
                    ("E1", "Elementary 2"),
                    ("E1", "Elementary 3"),
                    ("I1", "Intermediate 1"),
                    ("I2", "Intermediate 2"),
                    ("I3", "Intermediate 3"),
                    ("A1", "Advanced 1"),
                    ("A1", "Advanced 2"),
                    ("A1", "Advanced 3"),
                ],
                default=None,
                max_length=5,
            ),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="enrollments",
                to="school.student",
            ),
        ),
        migrations.AlterField(
            model_name="level",
            name="title",
            field=models.CharField(
                choices=[
                    ("S", "Starter"),
                    ("E", "Elementary"),
                    ("I", "Intermediate"),
                    ("A", "Advanced"),
                ],
                default=None,
                max_length=5,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="student", unique_together={("user", "id")},
        ),
    ]
