# Generated by Django 4.1.3 on 2022-12-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_ticket_date_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('RS', 'Решено'), ('UNRS', 'Не решено'), ('FZ', 'Заморожено')], default='UNRS', max_length=30, verbose_name='статус'),
        ),
    ]