# Generated by Django 2.1.7 on 2019-04-04 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'Página', 'verbose_name_plural': 'Páginas'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
