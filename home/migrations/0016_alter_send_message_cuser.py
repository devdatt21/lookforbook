# Generated by Django 4.1 on 2023-02-11 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_send_message_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_message',
            name='cuser',
            field=models.CharField(max_length=255),
        ),
    ]
