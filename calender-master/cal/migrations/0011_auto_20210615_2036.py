# Generated by Django 3.2.3 on 2021-06-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0010_auto_20210615_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='conf',
            new_name='Confirm',
        ),
        migrations.AlterField(
            model_name='confirm',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]