# Generated by Django 4.1.7 on 2023-03-04 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("common", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenity",
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
                ("name", models.CharField(max_length=150)),
                ("description", models.CharField(max_length=150, null=True)),
            ],
            bases=("common.commonmodel",),
        ),
        migrations.CreateModel(
            name="Room",
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
                ("price", models.PositiveIntegerField()),
                ("rooms", models.PositiveIntegerField()),
                ("toilets", models.PositiveIntegerField()),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=250)),
                ("pet_friendly", models.BooleanField(default=True)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("entire_place", "Entire Place"),
                            ("private_room", "Private Room"),
                            ("shared_room", "Shared Room"),
                        ],
                        max_length=20,
                    ),
                ),
                ("amenities", models.ManyToManyField(to="rooms.amenity")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("common.commonmodel",),
        ),
    ]
