# Generated by Django 2.1.1 on 2019-04-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyEva', '0006_performancerecord_blinkingfre'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
