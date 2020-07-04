# Generated by Django 3.0.6 on 2020-05-07 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mf', '0012_auto_20200507_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reviews', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mf.Reviews')),
            ],
        ),
    ]