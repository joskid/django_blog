from django.db import models
from django_blog.profiles.models import User

class Tag(models.Model):
        name=models.CharField(max_length=255)
        
        def __unicode__(self):
                return self.name
            
        class Meta:
            ordering = ['name']
        
class Category(models.Model):
        name=models.CharField(max_length=255)
        
        def __unicode__(self):
                return self.name
            
        class Meta:
            ordering = ['name']
            
class Live(models.Manager):
    """
    Customer Manager to only return Live post
    """

    def get_query_set(self):
        return super(Live, self).get_query_set().filter(status__exact=Post.LIVE_STATUS)
    
class Post(models.Model):
        # Statuses
        LIVE_STATUS = 1
        DRAFT_STATUS = 2
        HIDDEN_STATUS = 3
        
        statuses = (
                (LIVE_STATUS, 'Live'),
                (DRAFT_STATUS, 'Draft'),
                (HIDDEN_STATUS,'Hidden'),
        )
        
        title = models.CharField(max_length=255)
        slug = models.SlugField(unique_for_date="date_published")
        body = models.TextField()
        status = models.IntegerField(choices=statuses)        
        created_by = models.ForeignKey(User)

        categories = models.ManyToManyField(Category)
        tags = models.ManyToManyField(Tag)
        
        date_crated = models.DateTimeField(auto_now=True)
        date_modifed = models.DateTimeField(auto_now_add=True)
        date_published = models.DateTimeField()
        
        live = Live()
        objects = models.Manager()
        
        @models.permalink
        def get_absolute_url(self):
                return('post_detail', (), {
                    'year': self.date_published.strftime("%Y"),
                    'month': self.date_published.strftime("%b").lower(),
                    'day': self.date_published.strftime("%d"),
                    'slug': self.slug })
        
        def __unicode__(self):
                return self.title
        
        class Meta:
                ordering = ['-date_published']