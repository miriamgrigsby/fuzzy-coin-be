# Generated by Django 3.0.4 on 2020-03-27 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidfitness', '0019_auto_20200327_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]