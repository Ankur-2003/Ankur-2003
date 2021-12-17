from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=30)
    book_category = models.CharField(max_length=30, default="")
    book_id = models.AutoField
    book_cover = models.ImageField(upload_to='lib_books/images', default="")

    def __str__(self):
        return self.book_name