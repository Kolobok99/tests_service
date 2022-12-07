# Generated by Django 4.1.2 on 2022-12-07 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Время создания ')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Время добавления')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Время создания ')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Время добавления')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='tests.test')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Время создания ')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Время добавления')),
                ('title', models.CharField(max_length=256, verbose_name='Заголовок')),
                ('is_right', models.BooleanField(default=False, verbose_name='Правильный?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='tests.question')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответов',
            },
        ),
    ]
