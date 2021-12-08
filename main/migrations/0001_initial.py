# Generated by Django 3.2.9 on 2021-12-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(default='dog.svg', upload_to='pet_pics')),
                ('price', models.IntegerField(default=0)),
                ('reputation', models.IntegerField(default=0)),
            ],
        ),
    ]