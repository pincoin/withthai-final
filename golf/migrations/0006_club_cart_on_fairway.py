# Generated by Django 3.1.7 on 2021-03-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0005_auto_20210314_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='cart_on_fairway',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Cart on fairway'),
        ),
    ]
