# Generated by Django 3.1.7 on 2021-03-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golf', '0006_club_cart_on_fairway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='cart_compulsory_pax',
            field=models.IntegerField(db_index=True, default=0, verbose_name='Require golf cart pax+'),
        ),
    ]
