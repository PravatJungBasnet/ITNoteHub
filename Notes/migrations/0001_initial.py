# Generated by Django 5.0.1 on 2024-04-11 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.faculty')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notes.subject')),
            ],
        ),
    ]