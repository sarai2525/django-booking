# Generated by Django 2.2.9 on 2020-01-07 08:15

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
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='店名')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='表示名')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Store', verbose_name='店舗')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ログインユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='開始時間')),
                ('end', models.DateTimeField(verbose_name='終了時間')),
                ('name', models.CharField(max_length=255, verbose_name='予約者名')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Staff', verbose_name='スタッフ')),
            ],
        ),
        migrations.AddConstraint(
            model_name='staff',
            constraint=models.UniqueConstraint(fields=('user', 'store'), name='unique_staff'),
        ),
    ]
