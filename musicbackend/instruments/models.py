from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Подкатегории"
        verbose_name_plural = "Подкатегории"


class Img_for_instrument(models.Model):
    instrument_id = models.ForeignKey('Instruments', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return str(self.instrument_id)
    
    class Meta:
        verbose_name = "Фотографии муз инструментов"
        verbose_name_plural = "Фотографии муз инстр"


class Instruments(models.Model):
    article = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    characteristics = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    main_img = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Муз инструменты"
        verbose_name = "Муз инструменты"
    
    # def to_json(self):
    #     return {
    #         'id': self.id,
    #         'article': self.article,
    #         'name': self.name,
    #         'price': self.price,
    #         'description': self.description,
    #         'characteristics': self.characteristics,
    #         'category': self.category,
    #         'subcategory': self.subcategory,
    #         'main_img': self.main_img,
    #     }
        

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, default=None)
    img = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Request(models.Model):
    endpoint = models.CharField(max_length=100, null=True) # запрашиваемый урл
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    response_code = models.PositiveSmallIntegerField() # Response status code
    method = models.CharField(max_length=10, null=True)  # Request method
    remote_address = models.CharField(max_length=20, null=True)
    exec_time = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
    body_response = models.TextField() # Response data
    body_request = models.TextField() # Request data

    def __str__(self):
        return self.body_response

    class Meta:
        verbose_name = "Запрос"
        verbose_name_plural = "Запросы"
