from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    mobile = models.CharField(max_length=11, unique=True, blank=False, verbose_name='手机号')
    avatar = models.ImageField(max_length=256, upload_to='%Y%m%d/', blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        # 正序排序
        ordering = ('id',)

    def __str__(self):
        return self.username
