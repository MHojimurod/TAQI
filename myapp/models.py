from django.db import models

class NewsCategory(models.Model):
    name_uz    = models.CharField(max_length=200)
    name_ru    = models.CharField(max_length=200)
    name_en    = models.CharField(max_length=200)


    @property
    def json(self):
        return {
            "id": self.id,
            "name_uz": self.name_uz,
            "name_ru": self.name_ru,
            "name_en": self.name_en,
        }


class News(models.Model):
    news_category = models.ForeignKey(NewsCategory,on_delete=models.CASCADE)

    title_uz   = models.CharField(max_length=200)
    title_ru   = models.CharField(max_length=200)
    title_en   = models.CharField(max_length=200)
    image      = models.ImageField(upload_to="images/")

    desc_uz    = models.TextField()
    desc_ru    = models.TextField()
    desc_en    = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def json(self):
        return {
            "id":self.id,
            # "news_category":self.news_category.json,
            "title_uz": self.title_uz,
            "title_ru": self.title_ru,
            "title_en": self.title_en,
            "image": self.image.url,
            "desc_uz": self.desc_uz,
            "desc_ru": self.desc_ru,
            "desc_en": self.desc_en,
            "created_at": self.created_at,
        }
    def __str__(self):
        return self.title_uz
