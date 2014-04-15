from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200)


    def __unicode__(self):
        return self.title

    def get_tags(self):
        tgs = self.tags.split()
        return tgs
        
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

   

    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
