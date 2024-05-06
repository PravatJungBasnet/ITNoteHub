# Generated by Django 5.0.1 on 2024-05-06 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0007_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Notes.faculty'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chapter',
            name='semester',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Notes.semester'),
            preserve_default=False,
        ),
    ]
