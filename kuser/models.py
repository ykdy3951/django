from django.db import models

# Create your models here.


class Kuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    nickname = models.CharField(max_length=32, verbose_name='Nickname')
    password = models.CharField(max_length=128, verbose_name='비밀번호')
    level = models.CharField(max_length=8, verbose_name='등급',
                             choices=(
                                 ('3', 'admin'),
                                 ('2', 'seller'),
                                 ('1', 'user')
                             ))
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'kcw_kuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
