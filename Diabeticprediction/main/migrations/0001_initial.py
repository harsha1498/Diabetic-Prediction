# Generated by Django 5.0.1 on 2024-11-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_csv_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='Diabeticprediction\\main\\media')),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
