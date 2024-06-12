# Generated by Django 4.2.13 on 2024-06-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hottrack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True),
        ),
        migrations.AddIndex(
            model_name='song',
            index=models.Index(fields=['slug'], name='hottrack_so_slug_7cf104_idx'),
        ),
    ]
