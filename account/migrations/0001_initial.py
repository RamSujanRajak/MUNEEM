# Generated by Django 4.0.3 on 2022-04-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=100)),
                ('d_or_o', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('m_no', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]
