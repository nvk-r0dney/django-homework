# Generated by Django 5.0.3 on 2024-03-22 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Relationship",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "is_main",
                    models.BooleanField(default=False, verbose_name="Основной"),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="scopes",
                        to="articles.article",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тематика статьи",
                "verbose_name_plural": "Тематики статьи",
                "ordering": ["-is_main", "tag"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50, verbose_name="Тег")),
                (
                    "articles",
                    models.ManyToManyField(
                        related_name="tags",
                        through="articles.Relationship",
                        to="articles.article",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="relationship",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="scopes",
                to="articles.tag",
                verbose_name="Раздел",
            ),
        ),
    ]
