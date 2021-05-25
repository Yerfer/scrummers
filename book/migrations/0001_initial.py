# Generated by Django 3.2.3 on 2021-05-25 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('birthdate', models.DateField()),
                ('photo', models.ImageField(upload_to='authors_pfp/')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
                ('cover', models.ImageField(upload_to='book_cover/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
