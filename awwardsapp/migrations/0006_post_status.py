# Generated by Django 3.0.7 on 2020-06-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsapp', '0005_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0),
        ),
    ]
