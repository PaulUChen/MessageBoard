# Generated by Django 2.1.3 on 2019-02-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(default='', max_length=20)),
            ],
        ),
    ]