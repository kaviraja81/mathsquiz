# Generated by Django 3.0.8 on 2020-09-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0003_score_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='totalattempts',
            field=models.IntegerField(null=True),
        ),
    ]
