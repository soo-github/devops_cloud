from django.core.validators import RegexValidator
from django.db import models


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Shop(TimestampModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    telephone = models.CharField(max_length=14,
                                 validators=[
                                     RegexValidator(r"^\d{3}-?\d{4}-?\d{4}$", message="전화번호를 입력해주세요."),
                                 ],
                                 help_text="입력 예) 042-1234-1234")

    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"

    class Meta:
        ordering = ["-id"]


class Tag(TimestampModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"

    class Meta:
        ordering = ["name"]
