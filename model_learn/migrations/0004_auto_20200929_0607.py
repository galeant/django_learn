# Generated by Django 3.1.1 on 2020-09-29 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_learn', '0003_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activatio_limit', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_learn.product')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_learn.tag')),
            ],
            options={
                'db_table': 'product_tag',
            },
        ),
        migrations.RemoveField(
            model_name='tag',
            name='product',
        ),
        migrations.AddField(
            model_name='tag',
            name='product',
            field=models.ManyToManyField(related_name='tag', through='model_learn.ProductTag', to='model_learn.Product'),
        ),
    ]
