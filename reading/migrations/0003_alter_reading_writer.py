# Generated by Django 5.0 on 2023-12-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reading', '0002_alter_reading_memo_alter_reading_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='writer',
            field=models.CharField(max_length=30, verbose_name='著者'),
        ),
    ]
