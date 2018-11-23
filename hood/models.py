from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """Class that extends the user profile from django"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    bio = models.CharField(max_length=250)
    contact_info = models.CharField(max_length=250)

    @classmethod
    def get_user(cls, user):
        ask = cls.objects.filter(user=user)
        return ask

    @classmethod
    def update_profile(cls, id, bio, pic):
        upd8 = cls.objects.filter(user=id)
        upd8.bio = bio
        upd8.profile_pic = pic
        upd8.save()

    def save_profile(self):
        self.save()

    @classmethod
    def search_profiles(cls, search_term):
        return cls.objects.filter(user__username__icontains=search_term)

    @classmethod
    def delete_profile(cls, id):
        to_delete = cls.objects.filter(id=id)
        to_delete.delete()


