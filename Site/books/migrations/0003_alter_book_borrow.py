# Generated by Django 4.1.7 on 2023-10-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_borrow_book_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrow',
            field=models.CharField(max_length=50, null=True),
        ),
    ]