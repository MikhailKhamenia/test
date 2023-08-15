from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя писателя")

    def __str__(self):
        return self.name

class Reader(models.Model):
    last_name = models.CharField(max_length=100, default=None, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, default=None, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, default=None, verbose_name="Отчество")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

class Book(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name="Код книги")
    title = models.CharField(max_length=100, verbose_name="Название книги")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name="Картинка", default=None)
    def __str__(self):
        return self.title

class Borrowing(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    date_taken = models.DateField(verbose_name="Дата взятия книги")
    date_returned = models.DateField(null=True, blank=True, verbose_name="Дата возврата книги")

    def __str__(self):
        return f"{self.book} - {self.reader}"



