# Generated by Django 4.1.2 on 2023-06-01 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0006_alter_course_options_alter_course_title_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="grade",
            field=models.CharField(
                choices=[
                    ("a", "a"),
                    ("b", "b"),
                    ("c", "c"),
                    ("Not enrolled", "Not enrolled"),
                ],
                default="Not enrolled",
                max_length=15,
            ),
        ),
    ]