# Generated by Django 4.2.4 on 2023-08-30 01:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0009_alter_user_account_alter_user_nickname_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="nickname",
            new_name="username",
        ),
    ]