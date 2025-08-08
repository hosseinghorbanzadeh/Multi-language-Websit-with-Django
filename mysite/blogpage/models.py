from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = TaggableManager() 
    category = models.ManyToManyField(Category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_require=models.BooleanField(default=False)

    class Meta:
        ordering=['-created_date']

    def __str__(self):
        return self.title
    
    
    def snippet(self, num_words=10):
        words = self.content.split()  
        if len(words) <= num_words:  
            return self.content
        return ' '.join(words[:num_words]) + '...'
    
    def get_absolute_url(self):
        return reverse('blogpage:single', kwargs={'pid': self.id })
    



#======================== Start Class Comment ===============================
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email=models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approve = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-created_date']
    
   
#======================== End Class Comment =================================
        



    
  


