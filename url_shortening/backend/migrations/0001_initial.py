# Generated by Django 3.0.7 on 2020-06-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_link', models.URLField(verbose_name='Ссылка')),
                ('short_link', models.TextField(verbose_name='Сокращенная ссылка')),
                ('number_clicks', models.IntegerField(default=0, verbose_name='Число переходов')),
            ],
        ),
    ]
