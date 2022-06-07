# Generated by Django 4.0.5 on 2022-06-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('style', models.CharField(default='', max_length=256)),
                ('category', models.CharField(default='', max_length=256)),
                ('aroma', models.TextField(default='')),
                ('flavor', models.TextField(default='')),
                ('balance', models.TextField(default='')),
                ('season', models.TextField(default='')),
                ('paring_food', models.TextField(default='')),
                ('body', models.TextField(default='')),
                ('rating', models.FloatField(default=0.0)),
                ('img_url', models.ImageField(default='', upload_to='')),
            ],
            options={
                'db_table': 'Beer',
            },
        ),
    ]
