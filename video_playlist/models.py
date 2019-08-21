from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.



class voluntary_video(models.Model):
    title = models.CharField(max_length=30)
    video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="影片")
    poster_img = models.FileField(upload_to='image/', blank=True, null=True, verbose_name="預覽圖片")
    class Meta:
        verbose_name = _('voluntary_video')
        verbose_name_plural = _('志願役')
    def __str__(self):
        return self.title




class mandatory_video(models.Model):
    title = models.CharField(max_length=30)
    video = models.FileField(upload_to='videos/', blank=True, null=True, verbose_name="影片")
    poster_img = models.FileField(upload_to='image/', blank=True, null=True, verbose_name="預覽圖片")
    class Meta:
        verbose_name = _('mandatory_video')
        verbose_name_plural = _('軍事訓練役')

    def __str__(self):
        return self.title