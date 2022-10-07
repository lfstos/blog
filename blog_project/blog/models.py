from django.db import models
from django.template.defaultfilters import slugify


class Blog(models.Model):
    class PostSituation(models.TextChoices):
        DRAFT = 'D', 'Rascunho'
        PUBLISHED = 'P', 'Publicado'

    title = models.CharField(
        "Título",
        max_length=50
    )
    author = models.ForeignKey(
        "Author",
        on_delete=models.CASCADE
    )
    body = models.TextField(
        "Texto do Post",
        null=True, blank=True
    )
    publish = models.DateTimeField(
        "Publicação criada",
        auto_now_add=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    status = models.CharField(
        "Status da Publicação",
        max_length=1,
        choices=PostSituation.choices,
        default=PostSituation.DRAFT
    )

    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class Author(models.Model):
    name = models.CharField(
        "Nome do autor",
        max_length=50
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
