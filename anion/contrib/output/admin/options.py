from anion.contrib import admin

from ..models import (
    Article,
    Author,
    Award,
    Book,
    Contribution,
    Journal,
    Patent,
    Project,
)

__all__ = [
    "ArticleAdmin",
    "AuthorAdmin",
    "AwardAdmin",
    "BookAdmin",
    "ContributionAdmin",
    "JournalAdmin",
    "PatentAdmin",
    "ProjectAdmin",
]


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Journal` model.
    """


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Article` model.
    """


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Book` model.
    """


@admin.register(Patent)
class PatentAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Patent` model.
    """


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Project` model.
    """


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Award` model.
    """


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Author` model.
    """


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    """
    Admin options for the `output.Contribution` model.
    """
