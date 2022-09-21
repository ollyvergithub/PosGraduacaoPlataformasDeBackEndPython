from django.db import models


class Restaurant(models.Model):
    """Um objeto da classse Restaurant armazena informaçoes sobre um
       restaurante."""

    name = models.CharField(max_length=45)

    def __str__(self):
        return f"[Restaurant] name: {self.name}"


class MenuItem(models.Model):
    """Um objeto da classse MenuItem armazena informaçoes sobre um
       item de um menu de um restaurante."""
    category = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"[MenuItem] description: {self.description[:50]}"
