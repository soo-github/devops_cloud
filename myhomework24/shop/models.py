from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"

    class Meta:
        ordering =["-id"]


class Shop(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    telephone = models.CharField(max_length=13,
                                 validators=[
                                     RegexValidator(r"^\d{2,3}-?\d{3,4}-?\d{3,4}$",
                                                     message = "전화번호를 입력해주세요."),
                                 ],
                                 help_text = "입력예) 042-1234-1234")
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"

    class Meta:
        ordering =["-id"]


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"

    class Meta:
        ordering =["name"]


class Review(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"

    class Meta:
        ordering =["-id"]
