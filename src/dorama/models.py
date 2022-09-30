from django.db import models
from django.urls import reverse



class Dorama(models.Model):
    name = models.CharField(verbose_name="Название", 
                            max_length=250)
    image = models.ImageField(verbose_name="Изображение", 
                            upload_to="dorama/", 
                            blank=True)
    description = models.TextField(verbose_name="Описание")
    class Meta:
        verbose_name = "Дорама"
        verbose_name_plural = "Дорамы"
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("dorama:detail", kwargs={"pk": self.pk})
    