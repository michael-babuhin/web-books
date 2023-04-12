from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


@property
def is_overdue(self):
    if self.due_back and date.today() > self.due_back:
        return True
    return False

#Model of the book genre
class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите жанр книги",
                            verbose_name="Жанр книги")
    def __str__(self) -> str:
        return self.name


#Model for book language storage
class Language(models.Model):
    lang = models.CharField(max_length=30,
                            help_text="Введите текст книги",
                            verbose_name="Язык книги")
    def __str__(self) -> str:
        return self.lang


#A model for storing information about the author of a book
class Author(models.Model):
    first_name = models.CharField(max_length=30,
                                  help_text="Введите имя автора книги",
                                  verbose_name="Имя автора")
    second_name = models.CharField(max_length=30,
                                   help_text="Введите фамилию автора книги",
                                   verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения",
                                     verbose_name="Дата рождения",
                                     null=True,
                                     blank=True)
    date_of_death = models.DateField(help_text="Введите дату смерти",
                                     verbose_name="Дата смерти",
                                     null=True,
                                     blank=True)

    def __str__(self) -> str:
        return self.second_name


#Main model of the book
class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text="Введите название книги",
                             verbose_name="Название книги")
    genre = models.ForeignKey('Genre',
                              on_delete=models.CASCADE,
                              help_text="Введите жанр книги",
                              verbose_name="Жанр книги",
                              null=True)
    language = models.ForeignKey('Language',
                                 on_delete=models.CASCADE,
                                 help_text="Введите язык книги",
                                 verbose_name="Язык книги",
                                 null=True)
    author = models.ManyToManyField('Author',
                                    help_text="Введите автора книги",
                                    verbose_name="Автор книги")
    summary = models.TextField(max_length=1000,
                               help_text="Введите краткое описание книги",
                               verbose_name="Анотация книги")
    isbn = models.CharField(max_length=13,
                            help_text="Введите Isbn книги",
                            verbose_name="Isbn книги")

    def display_author(self):
        return ', '.join([author.second_name for author in self.author.all()])

    display_author.short_description = 'Автор'

    def __str__(self) -> str:
        return self.title

    """Returns the absolute url of the book to access the instance."""

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


#Model of book status
class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите статус книги",
                            verbose_name="Статус экземпляра книги")

    def __str__(self) -> str:
        return self.name


#Model Book Copy
class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    ivn_nom = models.CharField(max_length=20,
                                null=True,
                                help_text="Введите инвентарный экземпляр класса",
                                verbose_name="Инвентарный номер")
    publisher = models.CharField(max_length=20,
                                help_text="Введите издательство и год выпуска",
                                verbose_name="Издательство")
    status = models.ForeignKey('Status',
                               on_delete=models.CASCADE,
                               null=True,
                               help_text="Изменить состояние экземпляра",
                               verbose_name="Статус экземпляра книги")
    due_back = models.DateField(null=True,
                                blank=True,
                                help_text='Введите срок конца статуса',
                                verbose_name='Дата окончания статуса')
    borrower = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name='Заказчик',
                                 help_text='Выберите заказчика книги')


    def __str__(self) -> str:
        return f'{self.ivn_nom} {self.book} {self.status}'
