from anion.db import models


class AuthorManager(models.Manager):
    def get_by_natural_key(self, full_name):
        return self.get(full_name=full_name)


class Author(models.Model):
    full_name = models.CharField(max_length=255, unique=True)

    objects = AuthorManager()

    class Meta:
        app_label = "tests"

    def __str__(self):
        return self.full_name


class BookManager(models.Manager):
    def get_by_natural_key(self, title, author):
        return self.get(title=title, author=author)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, blank=True, null=True
    )

    objects = BookManager()

    class Meta:
        app_label = "tests"
        unique_together = [
            ("title", "author"),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"
