# Generated by Django 4.2.9 on 2024-02-07 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_remove_userprofile_birth_month'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'ordering': ['user_profile', 'address_id', 'created_on']},
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='user',
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user_profile',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to='profiles.userprofile'),
            preserve_default=False,
        ),
    ]