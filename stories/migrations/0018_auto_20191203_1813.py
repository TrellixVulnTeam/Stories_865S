# Generated by Django 2.2.7 on 2019-12-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0017_auto_20191203_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]