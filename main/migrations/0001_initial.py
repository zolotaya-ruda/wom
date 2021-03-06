# Generated by Django 3.1 on 2020-10-24 17:31

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
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='new_sg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.CharField(max_length=50, verbose_name='Песня')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('add_mus', models.FileField(default='', upload_to='arch/for_main', verbose_name='Файл')),
                ('views', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Артист')),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='rub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserSongRalation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False, null=True)),
                ('media', models.BooleanField(default=False, null=True)),
                ('track', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.new_sg')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='opisan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='О себе:')),
                ('artist', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='main.city', verbose_name='Город')),
            ],
        ),
        migrations.AddField(
            model_name='new_sg',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='main.rub', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='new_sg',
            name='potr',
            field=models.ManyToManyField(related_name='potr', through='main.UserSongRalation', to=settings.AUTH_USER_MODEL),
        ),
    ]
