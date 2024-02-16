# Generated by Django 4.2.9 on 2024-02-15 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('ABOUT', 'About Section'), ('FAQ', 'Frequently Asked Questions'), ('ENQUIRY', 'Customer Enquiry Text')], default='ABOUT', max_length=7)),
                ('disp_seq', models.IntegerField(default=10)),
                ('hide_display', models.BooleanField(default=False)),
                ('section_title', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['disp_seq'],
            },
        ),
        migrations.CreateModel(
            name='AboutText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disp_seq', models.IntegerField(default=10)),
                ('hide_display', models.BooleanField(default=False)),
                ('text_title', models.CharField(max_length=50)),
                ('text_body', models.TextField(blank=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_section', to='home.aboutsection')),
            ],
            options={
                'ordering': ['disp_seq'],
            },
        ),
    ]