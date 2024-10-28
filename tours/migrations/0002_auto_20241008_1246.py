# Generated by Django 3.2.16 on 2024-10-08 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'default_related_name': 'tours', 'ordering': ('price',), 'verbose_name': 'тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.AddField(
            model_name='location',
            name='county',
            field=models.CharField(default=None, max_length=256, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='image',
            field=models.ImageField(blank=True, upload_to='tour_images', verbose_name='Фото'),
        ),
    ]