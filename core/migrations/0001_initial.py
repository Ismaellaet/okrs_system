# Generated by Django 4.1.2 on 2022-10-25 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OKR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objective', models.CharField(max_length=150)),
                ('key_result_1', models.CharField(max_length=200, verbose_name='key result 1')),
                ('key_result_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='key result 2')),
                ('key_result_3', models.CharField(blank=True, max_length=200, null=True, verbose_name='key result 3')),
                ('key_result_4', models.CharField(blank=True, max_length=200, null=True, verbose_name='key result 4')),
                ('key_result_5', models.CharField(blank=True, max_length=200, null=True, verbose_name='key result 5')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.member')),
            ],
        ),
    ]
