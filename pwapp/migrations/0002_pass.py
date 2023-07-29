# Generated by Django 4.2.3 on 2023-07-29 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pwapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pwapp.user')),
            ],
        ),
    ]