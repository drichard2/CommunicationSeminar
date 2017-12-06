# Generated by Django 2.0 on 2017-12-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComSemApp', '0013_auto_20171204_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='frequency',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='frequency',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expression',
            name='reformulation_audio',
            field=models.BooleanField(default=False),
        ),
    ]
