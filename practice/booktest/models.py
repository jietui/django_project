from django.db import models
from django.db.models import F, Q
from django.db.models import Sum, Min, Max, Avg, Count

# Create your models here.
# 自定义图书管理器
class BookInfoManager(models.Manager):
    def all(self):
        return super(BookInfoManager, self).all().filter(is_delete=False)

    def create_book(self, title, pub_date, read=0, comment=0, is_delete=False):
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = read
        book.bcomment = comment
        book.is_delete = is_delete
        book.save()
        return book


class BookInfo(models.Model):
    # 模型中定义管理器
    books = BookInfoManager()

    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_books'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'famale'),
        (1, 'male')
    )
    hname = models.CharField(max_length=20, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heroes'
        verbose_name = "英雄"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname
