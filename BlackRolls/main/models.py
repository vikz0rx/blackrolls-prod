from django.db import models
from django.utils.translation import ugettext_lazy as _

class FoodKind(models.Model):
    title = models.CharField(_('Название'), max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('категорию блюда')
        verbose_name_plural = _('Категории блюд')

class Food(models.Model):
    kind = models.ForeignKey(FoodKind, on_delete=models.CASCADE, related_name='kind', verbose_name='Категория блюда')
    title = models.CharField(_('Название'), max_length=128)
    description = models.CharField(_('Описание'), max_length=512, blank=True, null=True)
    cost = models.PositiveSmallIntegerField(_('Цена'), )
    cost_on_sale = models.PositiveSmallIntegerField(_('Цена cо скидкой'), blank=True, null=True)
    weight = models.PositiveSmallIntegerField(_('Вес'), )
    image = models.ImageField(_('Изображение'), upload_to='food')
    is_hot = models.BooleanField(_('Острое?'), default=False)

    def __str__(self):
        return self.title

    def get_sale_amount(self):
        if self.cost_on_sale:
            return self.cost - self.cost_on_sale
        else:
            return None

    class Meta:
        verbose_name = _('блюдо')
        verbose_name_plural = _('Блюда')