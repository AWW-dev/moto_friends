# Generated by Django 3.0.6 on 2020-05-07 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mf', '0007_commenttrip'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenttrip',
            name='trip',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mf.Trip'),
            preserve_default=False,
        ),
    ]
