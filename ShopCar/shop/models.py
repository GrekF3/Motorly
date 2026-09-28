from colorfield.fields import ColorField
from django.db import models


class MarkAuto(models.Model):
    mark = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.mark


class ModelAuto(models.Model):
    mark = models.ForeignKey(MarkAuto, on_delete=models.PROTECT)
    model = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.model


class Auto(models.Model):
    COLOR_PALETTE = [
        ("#FFFFFF", "white",),
        ("#000000", "black",),
        ("#C0C0C0", "silver"),
        ("#00D678", "green"),
        ("#808080", "gray"),
        ("#FF0000", "red"),
        ("#0000ff", "blue"),
        ("#ffff00", "yellow"),
    ]

    mark = models.ForeignKey(MarkAuto, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelAuto, on_delete=models.CASCADE)
    color = ColorField(samples=COLOR_PALETTE)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'




class Order(models.Model):
    seller = models.CharField(max_length=255, default=None)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = "Заказы"
