from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    Model for a Blog Post
    Each blog post will have a title,
    publication date, body, and image field
    """
    title = models.CharField(max_length=200, default=f"Post Title")
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title