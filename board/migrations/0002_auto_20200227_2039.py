# Generated by Django 3.0.3 on 2020-02-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='contents',
            field=models.TextField(verbose_name='게시글'),
        ),
    ]
