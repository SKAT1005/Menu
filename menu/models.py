from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=512)
    menu = models.ForeignKey('Menu', blank=True, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
