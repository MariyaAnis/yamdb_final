from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validator import valid_year


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = (
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    )

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    username = models.CharField(
        'Логин',
        blank=False,
        unique=True,
        max_length=150,
        help_text='Поле обязательно, максимум 150 символов.',
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=ROLES,
        default=USER
    )
    bio = models.TextField(
        verbose_name='О себе',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_is_not_me'
            )
        ]


class Genres(models.Model):
    name = models.CharField('Заголовок', max_length=265)
    slug = models.SlugField('Слаг', max_length=50, unique=True)

    class Meta:
        ordering = ('slug',)


class Categories(models.Model):
    name = models.CharField('Заголовок', max_length=265)
    slug = models.SlugField('Слаг', max_length=50, unique=True)

    class Meta:
        ordering = ('slug',)


class Title(models.Model):
    name = models.CharField('Заголовок', max_length=200, unique=True)
    year = models.SmallIntegerField(
        validators=[valid_year]
    )
    description = models.TextField('Описание')
    genre = models.ManyToManyField(
        Genres,
        verbose_name='Жанры',
        related_name='title',
    )
    category = models.ForeignKey(
        Categories,
        verbose_name='Категории',
        on_delete=models.PROTECT,
        related_name='title',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг',
        validators=[
            MinValueValidator(1, 'Допустимы значения от 1 до 10'),
            MaxValueValidator(10, 'Допустимы значения от 1 до 10')
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author',),
                name='unique_review'
            ),
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('pub_date',)
