# Generated by Django 4.2.13 on 2024-07-09 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_memo_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemoGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='memo',
            name='author',
        ),
        migrations.AddField(
            model_name='memo',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.memogroup'),
            preserve_default=False,
        ),
    ]
