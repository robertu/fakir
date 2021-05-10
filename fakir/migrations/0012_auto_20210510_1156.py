# Generated by Django 3.2 on 2021-05-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakir', '0011_auto_20210510_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicznikFaktur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podatek', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='faktura',
            name='J_M',
            field=models.CharField(choices=[('1', 'Godzina'), ('2', 'Sztuka')], default='2', max_length=200, verbose_name='J.M'),
        ),
    ]
