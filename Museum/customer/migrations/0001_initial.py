# Generated by Django 4.0.5 on 2022-06-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('des', models.TextField()),
                ('img', models.ImageField(upload_to='pics')),
                ('offer', models.BooleanField(default=False)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
