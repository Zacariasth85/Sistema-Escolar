# Generated by Django 5.1.3 on 2024-12-03 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('area_de_atuacao', models.CharField(max_length=100)),
                ('tempo_de_experiencia', models.IntegerField()),
            ],
        ),
    ]
