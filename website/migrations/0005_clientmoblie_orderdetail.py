# Generated by Django 2.2.6 on 2020-09-17 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200909_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientMoblie',
            fields=[
                ('clientMoblieId', models.AutoField(primary_key=True, serialize=False)),
                ('clientMoblieNumber', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_Items', models.CharField(max_length=10000)),
                ('order_Total', models.CharField(max_length=50)),
                ('c_Name', models.CharField(max_length=50)),
                ('c_Moblie', models.CharField(max_length=50)),
                ('c_AltMoblie', models.CharField(max_length=50)),
                ('c_Address', models.CharField(max_length=50)),
                ('c_Address2', models.CharField(max_length=50)),
                ('c_Email', models.CharField(max_length=50)),
                ('c_State', models.CharField(max_length=50)),
                ('c_City', models.CharField(max_length=50)),
                ('c_Zip', models.CharField(max_length=50)),
                ('Date', models.DateField()),
            ],
        ),
    ]
