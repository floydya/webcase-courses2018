from django.contrib.auth.models import User
from django.db import models
import os

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


def path_and_rename(instance, filename):
    upload_to = 'user_avatars'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class Profile(models.Model):
    """
    Расширение модели пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to=path_and_rename, verbose_name='Аватар', blank=True, null=True)

    followers = models.ManyToManyField(User, blank=True, related_name='followed_to')

    def get_absolute_url(self):
        return reverse('profile', args=[self.user.username])


@receiver(post_save, sender=User)
def create_save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
