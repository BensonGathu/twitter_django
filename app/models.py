from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    user_name = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    phone_number= models.IntegerField( blank=True, null=True)
    #profile_pic = models.FileField(blank=True,null=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.user_name


    def save_user(self):
        self.save()




# class Tweet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null = True)
#     tweetImages = 
#     description = models.CharField(max_length=20, blank=True, null=True)
#     likes= models.ManyToManyField(User)
#     views= models.ManyToManyField(User)
#     retweets= models.ManyToManyField(User)
#     datePublished=models.DateTimeField(auto_now_add=True)



   
    
    # required this.datePublished,
    # required this.tweetId,
    # required this.tweetUrl,
    # required this.likes,
    # required this.views,
    # required this.retweets