from django.db import models


class Author(models.Model):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    name = models.CharField(max_length=256)
    description = models.TextField()
    birthdate = models.DateField()
    photo = models.ImageField(upload_to='authors_pfp/')


class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    title = models.CharField(max_length=256)
    isbn = models.CharField(max_length=13, verbose_name='ISBN')
    cover = models.ImageField(upload_to='book_cover/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False, null=False)
