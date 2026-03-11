from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=get_user_model())

def create_user_profile(sender, instance, created , **kwargs):

    if created:

        if not instance.bio:
            instance.bio = "New user joined the blog"

        instance.save()

        print(f"Signal Triggered: CustomUser created for {instance.username}")

@receiver(post_save, sender = Post)
def create_post(sender, instance, created , **kwargs):

    if created:

        print(f"POST CREATED SUCCESSFULLY WITH TITLE {instance.title} and by {instance.author}")        




