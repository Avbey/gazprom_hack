# Generated by Django 2.2.2 on 2020-10-17 19:21

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TaskState",
            fields=[
                ("slug", models.SlugField(max_length=2, primary_key=True, serialize=False)),
                ("name", models.CharField(db_index=True, max_length=100)),
                (
                    "stype",
                    models.PositiveIntegerField(
                        choices=[(0, "Unstarted"), (1, "Started"), (2, "Done"), (3, "KP")], db_index=True, default=0
                    ),
                ),
            ],
            options={"verbose_name": "Статус заказа", "verbose_name_plural": "Статусы заказа",},
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("date", models.DateField(verbose_name="Дата")),
                ("comment", tinymce.models.HTMLField(blank=True, null=True, verbose_name="Комментарий")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Обновлено")),
                (
                    "state",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tenders.TaskState",
                        verbose_name="Статус",
                    ),
                ),
            ],
            options={"verbose_name": "Задача", "verbose_name_plural": "Задачи", "ordering": ["date"],},
        ),
    ]
