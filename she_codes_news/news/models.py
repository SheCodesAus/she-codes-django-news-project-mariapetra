from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.forms import CharField

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return(self.name)

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField() 
    image=models.URLField(null=True, blank=True)
    category = models.ForeignKey(
            Category, 
            related_name = "stories",
            null = True, blank=True,
            on_delete=models.SET_NULL
        )
    class Meta: 
        ordering = ['-pub_date']

    # categories = (
    #     ("NEWS", "News"),
    #     ("CUPCAKES", "Cupcakes"),
    #     ("THINGS", "Things"),
    # )

   

