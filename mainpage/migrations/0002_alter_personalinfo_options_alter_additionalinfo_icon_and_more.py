# Generated by Django 5.1.2 on 2024-10-15 15:19

import mainpage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalinfo',
            options={'verbose_name': 'Персональная информация', 'verbose_name_plural': 'Персональная информация'},
        ),
        migrations.AlterField(
            model_name='additionalinfo',
            name='icon',
            field=models.ImageField(upload_to=mainpage.models.upload_to_common, verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='image',
            field=models.ImageField(null=True, upload_to=mainpage.models.upload_to_common, verbose_name='Картинка баннера'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='image_mobile',
            field=models.ImageField(null=True, upload_to=mainpage.models.upload_to_common, verbose_name='Картинка баннера для мобилки'),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='resume_file',
            field=models.FileField(upload_to=mainpage.models.upload_to_common, verbose_name='Файл резюме'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to=mainpage.models.upload_to_common, verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='image_mobile',
            field=models.ImageField(upload_to=mainpage.models.upload_to_common, verbose_name='Картинка для мобилки'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='icon',
            field=models.ImageField(upload_to=mainpage.models.upload_to_common, verbose_name='Иконка компании'),
        ),
    ]