# Generated by Django 4.0.3 on 2023-06-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20200507_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_count',
            field=models.IntegerField(default=0),
        ),
    ]
