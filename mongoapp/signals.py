from . models import BlogPost

from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from django.utils.text import slugify

@receiver(post_save,sender=BlogPost)
def post_save_create_slug(sender,instance,created,*args,**kwargs):
    if not instance.slug:
        instance.slug=slugify(instance.title)
        instance.save()