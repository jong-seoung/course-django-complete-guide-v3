# Generated by Django 5.0.7 on 2024-07-25 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photolog', '0002_alter_note_options_note_tags_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pk']},
        ),
    ]