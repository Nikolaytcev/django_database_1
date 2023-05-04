from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.ImageField(max_length=200)
    release_date = models.CharField(default=None, max_length=20)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(default=None, max_length=255, unique=True, db_index=True, verbose_name="URL")

