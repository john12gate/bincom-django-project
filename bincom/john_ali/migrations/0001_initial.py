# Generated by Django 4.2.3 on 2023-07-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BincomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agentname', models.CharField(max_length=200)),
                ('announced_lga_results', models.IntegerField()),
                ('announced_pu_results', models.IntegerField()),
                ('announced_state_results', models.IntegerField()),
                ('announced_ward_results', models.IntegerField()),
                ('lga', models.CharField(max_length=200)),
                ('party', models.CharField(max_length=200)),
                ('polling_unit', models.CharField(max_length=200)),
                ('states', models.CharField(max_length=200)),
                ('ward', models.CharField(max_length=200)),
            ],
        ),
    ]
