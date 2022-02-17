# Generated by Django 4.0.1 on 2022-02-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_newsstory_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='newsstory',
            name='category',
        ),
    ]