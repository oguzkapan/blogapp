# Generated by Django 3.2.9 on 2023-10-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_blog_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_img',
            field=models.ImageField(null=True, upload_to='category'),
        ),
    ]
