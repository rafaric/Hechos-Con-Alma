# Generated by Django 4.0.6 on 2022-08-03 19:56

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
            name='Post',
            fields=[
                ('idPost', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('fechahora', models.DateTimeField(auto_now_add=True)),
                ('textoLargo', models.TextField()),
                ('contador', models.IntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='posts/img')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-fechahora'],
            },
        ),
    ]