# Generated by Django 4.1.5 on 2023-04-08 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aquaponic_guide', '0002_alter_manual_sub_chapter_content_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manual_chapter',
            old_name='Chapter_name',
            new_name='name',
        ),
    ]
