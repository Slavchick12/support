# Generated by Django 4.1.3 on 2022-12-06 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'Обращение', 'verbose_name_plural': 'Обращения'},
        ),
        migrations.AlterModelOptions(
            name='ticketresponse',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.RemoveConstraint(
            model_name='ticketresponse',
            name='message_unique',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='ticketresponse',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='tickets.ticketresponse', verbose_name='ответ'),
        ),
        migrations.AlterField(
            model_name='ticketresponse',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='tickets.ticket', verbose_name='обращение'),
        ),
    ]
