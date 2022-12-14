# Generated by Django 4.0.4 on 2022-06-22 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('religion', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=50)),
                ('gaurdian_name', models.CharField(max_length=50)),
                ('gaurdian_income', models.IntegerField()),
                ('name_of_school', models.CharField(max_length=50)),
                ('matric_marks', models.IntegerField()),
                ('year_of_matric', models.IntegerField()),
                ('matric_grade', models.CharField(max_length=10)),
                ('matric_board', models.CharField(max_length=50)),
                ('name_of_college', models.CharField(max_length=50)),
                ('inter_marks', models.IntegerField()),
                ('year_of_inter', models.IntegerField()),
                ('inter_grade', models.CharField(max_length=10)),
                ('inter_board', models.CharField(max_length=50)),
                ('university_name', models.CharField(max_length=50)),
                ('field_of_interest', models.CharField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
