# Generated by Django 2.0.3 on 2018-03-10 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ('created', 'owner')},
        ),
    ]
