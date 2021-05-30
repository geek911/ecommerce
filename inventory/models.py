from django.db import models


class Entity(models.Model):
    """
    All objects which will be added to the system will inherit
    from this object.
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Entity):
    """
    This are the categories of the product
    """
    name = models.CharField(max_length=200)

    class Meta(Entity.Meta):
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(Entity):
    """
    These are product details
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # image = mod

    class Meta(Entity.Meta):
        ordering = ['-created_on']

    def __str__(self):
        return self.name
