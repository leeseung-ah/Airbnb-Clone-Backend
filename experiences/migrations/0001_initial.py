# Generated by Django 4.1.7 on 2023-03-05 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Perk",
            fields=[
                (
                    "commonmodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="common.commonmodel",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("details", models.CharField(max_length=250)),
                ("explanation", models.TextField()),
            ],
            bases=("common.commonmodel",),
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "commonmodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="common.commonmodel",
                    ),
                ),
                ("country", models.CharField(default="한국", max_length=50)),
                ("city", models.CharField(default="서울", max_length=80)),
                ("name", models.CharField(max_length=250)),
                ("price", models.PositiveIntegerField()),
                ("address", models.CharField(max_length=250)),
                ("start", models.TimeField()),
                ("end", models.TimeField()),
                ("description", models.TextField()),
                (
                    "host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("perks", models.ManyToManyField(to="experiences.perk")),
            ],
            bases=("common.commonmodel",),
        ),
    ]
