# Generated by Django 4.1.5 on 2023-02-26 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogovor_online', '0002_alter_dogovor_options_alter_objectbydogovor_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dogovor',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
