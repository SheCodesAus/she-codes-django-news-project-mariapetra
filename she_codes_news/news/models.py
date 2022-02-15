from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField() 
    class Meta: 
        ordering = ['-pub_date']



    categories = (
        ("NEWS", "News"),
        ("CUPCAKES", "Cupcakes"),
        ("THINGS", "Things"),
    )

    category = models.CharField(max_length=200, choices = categories, default="News")
