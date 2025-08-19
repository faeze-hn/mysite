from django.db import models

class post(models.Model):
    #image
    #author
    title = models.CharField(max_length=225)
    content = models.TextField()
    #tags
    #category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null = True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.id}'