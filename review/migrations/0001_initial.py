# Generated by Django 3.0.3 on 2020-02-28 23:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trail', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('review', models.CharField(max_length=250)),
                ('stars', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trail.Trail')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
