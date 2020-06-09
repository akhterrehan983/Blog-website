from django.db import models
class User(models.Model):
    address    = models.CharField(max_length=500)
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    email    = models.EmailField(primary_key=True)
    password = models.CharField(max_length=15)
    phone_no= models.IntegerField()
    gender  = models.CharField(max_length=20)
    profile_pic =models.ImageField(upload_to="images",default="images/blankprofile.webp",blank=True)
class Post(models.Model):
    email= models.EmailField(blank=True)
    blog_heading = models.CharField(max_length=100)
    description  = models.CharField(max_length=1000)
    datetime     = models.DateTimeField(auto_now_add=True)
    likes_count  = models.IntegerField(default=0)
    comment      = models.CharField(blank=True,max_length=200)
    post_pic     = models.URLField(blank=True)
class Liked_post(models.Model):
    post_id = models.IntegerField()
    liker_email = models.EmailField()
    is_liked = models.BooleanField()
class Comment_post(models.Model):
    post_id = models.IntegerField()
    commenter_email = models.EmailField()
    comment = models.CharField(max_length=1000)
    datetime= models.DateTimeField(auto_now_add=True)
    commenter_pic = models.URLField(blank=True)

    
