# Generated by Django 3.2.7 on 2022-05-04 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Chairman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('ID_pic', models.FileField(default='media/default.png', upload_to='media/documents')),
                ('profile_pic', models.FileField(default='media/default.png', upload_to='media/images')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Chairman.user')),
            ],
        ),
    ]
