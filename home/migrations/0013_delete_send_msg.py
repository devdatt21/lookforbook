# Generated by Django 4.1 on 2023-02-11 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_send_msg_delete_store_msg'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Send_msg',
        ),
    ]