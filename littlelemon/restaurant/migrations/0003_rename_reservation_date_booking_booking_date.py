# Generated by Django 4.1.5 on 2023-08-26 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests_alter_menu_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='reservation_date',
            new_name='booking_date',
        ),
    ]
