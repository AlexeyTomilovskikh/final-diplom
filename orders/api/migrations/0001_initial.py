# Generated by Django 2.2.13 on 2021-11-21 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email пользователя')),
                ('username', models.CharField(blank=True, max_length=100, verbose_name='Имя Пользователя')),
                ('usertype', models.CharField(choices=[('shop', 'Магазин'), ('buyer', 'Покупатель')], max_length=50, verbose_name='Тип пользователя')),
                ('is_activated', models.BooleanField(default=False, verbose_name='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'auth_user',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='ModelParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150, verbose_name='Значение характеристики')),
            ],
            options={
                'verbose_name': 'Значение характеристики',
                'verbose_name_plural': 'Значения характеристик',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('basket', 'В корзине'), ('new', 'Новый'), ('accepted', 'Принят в обработку'), ('ready', 'Собран, ждет отправки'), ('sent', 'Отправлен'), ('delivered', 'Доставлен')], max_length=50, verbose_name='Статус заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Характеристика')),
            ],
            options={
                'verbose_name': 'Характеристика',
                'verbose_name_plural': 'Характеристики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='api.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.URLField(verbose_name='Источник данных')),
                ('status', models.BooleanField(default=True, verbose_name='Работает ли магазин')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='api.Product', verbose_name='Товар')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='api.Shop', verbose_name='Магазин')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='api.Order', verbose_name='Заказ')),
                ('parameters', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_items', to='api.ModelParameter', verbose_name='Характеристики')),
            ],
            options={
                'verbose_name': 'Заказанный товар',
                'verbose_name_plural': 'Заказанные товары',
            },
        ),
        migrations.AddField(
            model_name='modelparameter',
            name='parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_parameter', to='api.Parameter', verbose_name='Характеристика'),
        ),
        migrations.AddField(
            model_name='modelparameter',
            name='product_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_parameter', to='api.ProductModel', verbose_name='Модель'),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=150, verbose_name='Улица')),
                ('house', models.CharField(max_length=30, verbose_name='Дом')),
                ('apartment', models.CharField(blank=True, max_length=10, verbose_name='Квартира')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона пользователя')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL, verbose_name='Ползователь')),
            ],
            options={
                'verbose_name': 'Контакты',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='shops',
            field=models.ManyToManyField(blank=True, related_name='categories', to='api.Shop', verbose_name='Магазины'),
        ),
        migrations.AddConstraint(
            model_name='productmodel',
            constraint=models.UniqueConstraint(fields=('product', 'shop'), name='unique_model_in_shop'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order', 'parameters'), name='unique_product_in_order'),
        ),
        migrations.AddConstraint(
            model_name='modelparameter',
            constraint=models.UniqueConstraint(fields=('parameter', 'product_model'), name='unique_parameter_of_model'),
        ),
    ]
