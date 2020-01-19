# Generated by Django 2.1.5 on 2020-01-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=50)),
                ('dateofjoining', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=200)),
                ('phonenumber', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('eid', 'designation', 'dateofjoining', 'name', 'address', 'phonenumber', 'email')},
        ),
    ]