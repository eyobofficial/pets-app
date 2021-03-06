# Generated by Django 2.0.1 on 2018-01-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet',
            options={'ordering': ['owner', 'name']},
        ),
        migrations.AlterField(
            model_name='pet',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='kind',
            field=models.CharField(choices=[('cat', 'Cat'), ('dog', 'Dog')], max_length=8, verbose_name='Pet Type'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
