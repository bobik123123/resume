# Generated by Django 5.1.2 on 2024-10-24 10:52

import mainpage.utilts
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0004_additionalinfo_personal_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='resume_file',
            field=models.FileField(blank=True, null=True, upload_to=mainpage.utilts.upload_to_common, verbose_name='Файл резюме'),
        ),
    ]
