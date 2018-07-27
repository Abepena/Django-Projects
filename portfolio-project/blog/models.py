from django.db import models

# Create your models here.
class Blog(models.Model):
    """
    Model for a Blog Post
    Each blog post will have a title,
    publication date, body, and image field
    """
    title = models.CharField(max_length=200, default="Post Title")
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        #Shows only the first 200 characters of a blog post
        return self.body[:200]

    def date_only(self):
        #Customizes pub_date field to how you want it to look exactly
        #based on datetime.datetime
        #Reference: http://strftime.org/
        return self.pub_date.strftime('%A %B %d, %Y')
