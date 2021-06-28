from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.lookups import In
from mongoProject import settings
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save,pre_delete,post_delete

from django.utils.text import slugify

# User=settings.AUTH_USER_MODEL

# Create your models here.


class UserData(models.Model):
    name=CharField(max_length=120)
    age=IntegerField()


class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(blank=True,null=True)
    created_at=models.DateTimeField(blank=True,null=True,auto_now_add=True)    


    def __str__(self):
        return self.title




# django signals

#1.the better way to to connect reciever and User model

#before save in to db, it does not contain created parameter
@receiver(pre_save,sender=User)
def pre_save_reciever(sender,instance,*args,**kwargs):
    """
    dont have created parameter, before save into databse
    """
    print(instance.username,instance.id)  # id is None because "id" will get after saved database but name will get
    # print(args)
    # print("keywoord args")
    # print(kwargs)


#after save in to db ,so it have create parameter TRUE
@receiver(post_save,sender=User)
def post_save_reciever(sender,instance,created,*args,**kwargs):
    if created:
        print("send email to",instance.username)
        #trigger pre save work again
        instance.save()
        # trigger post save work again
    else:
        print(instance.username,"just saved")    
    print(args)
    print("keywoord args")
    print(kwargs)

 


#2.another way

# post_save.connect(user_created_model,sender=User)



@receiver(pre_save,sender=BlogPost)
def pre_save_create(sender,instance,*args,**kwargs):
    print("before saving to database")       



@receiver(post_save,sender=BlogPost)
def post_save_create_slug(sender,instance,created,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)
        instance.save()   

@receiver(pre_delete,sender=BlogPost)
def pre_delete_signal(sender,instance,*args,**kwargs):
    print("before delete into database")     

@receiver(post_delete,sender=BlogPost)
def post_delete_signal(sender,instance,*args,**kwargs):
    print("after delete into database")      


      

