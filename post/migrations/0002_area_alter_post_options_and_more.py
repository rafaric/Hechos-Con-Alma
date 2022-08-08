# Generated by Django 4.0.6 on 2022-08-03 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fechaHora']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='fechahora',
            new_name='fechaHora',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='idPost',
            new_name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, default='null', upload_to='posts/img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.area'),
            preserve_default=False,
        ),
    ]