# Generated by Django 4.1.1 on 2022-09-29 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_stack_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='dev',
            new_name='stack',
        ),
    ]