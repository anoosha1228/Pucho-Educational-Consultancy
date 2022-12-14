# Generated by Django 4.0.6 on 2022-07-22 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(blank=True, max_length=50)),
                ('program_name', models.CharField(max_length=50)),
                ('program_abbreviation', models.CharField(max_length=10)),
                ('last_merit', models.CharField(max_length=50)),
                ('eligibilty_criteria', models.CharField(max_length=1500)),
                ('fee_structure', models.IntegerField()),
            ],
        ),
    ]
