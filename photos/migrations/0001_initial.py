# Generated by Django 3.1.7 on 2021-04-03 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('desc', models.TextField()),
                ('width', models.CharField(choices=[('0', '4x1'), ('width-1', '3x1'), ('width-2', '2x1')], max_length=10)),
                ('img', models.ImageField(upload_to='photos/')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]