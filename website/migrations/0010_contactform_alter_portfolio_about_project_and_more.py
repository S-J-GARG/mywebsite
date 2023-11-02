# Generated by Django 4.2.6 on 2023-11-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_myblog_blog_alter_portfolio_portfolio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont_name', models.CharField(default='Ram', max_length=100, null=True)),
                ('cont_email', models.CharField(default='Ram', max_length=100, null=True)),
                ('query', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='about_project',
            field=models.CharField(max_length=350),
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]
