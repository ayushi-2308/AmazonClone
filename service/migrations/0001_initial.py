# Generated by Django 5.0.1 on 2024-03-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mediaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj1', models.CharField(max_length=90)),
                ('obj2', models.FileField(default=None, null=True, upload_to='Media/')),
            ],
        ),
    ]
