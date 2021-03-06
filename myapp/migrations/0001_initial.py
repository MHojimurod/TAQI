# Generated by Django 4.0.2 on 2022-02-02 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(max_length=200)),
                ('name_ru', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=200)),
                ('title_ru', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('desc_uz', models.TextField()),
                ('desc_ru', models.TextField()),
                ('desc_en', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.newscategory')),
            ],
        ),
    ]
