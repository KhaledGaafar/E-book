# Generated by Django 4.1.7 on 2023-10-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_book_student_borrowbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrow',
            field=models.IntegerField(),
        ),
    ]