# Generated by Django 4.0.3 on 2022-03-04 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('initial_capital', models.IntegerField()),
                ('accumulated_capital', models.IntegerField()),
                ('starupper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.startupper')),
            ],
        ),
    ]
