from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
   if created:
       Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
   instance.profile.save()


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



class Neighborhood(models.Model):
    """Class defining the neighborhood model"""
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    occupants = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1,null = True)

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.filter(pk=id)
        neighbourhoods.delete()

    @classmethod
    def get_neighbourhood_by_id(cls, id):
        neighbourhoods = cls.objects.get(pk=id)
        return neighbourhoods

    @classmethod
    def filter_by_location(cls, location):
        neighbourhoods = cls.objects.filter(location=location)
        return neighbourhoods

    @classmethod
    def search_neighbourhood(cls, search_term):
        neighbourhoods = cls.objects.filter(neighbourhood_name__icontains=search_term)
        return neighbourhoods

class Post(models.Model):
    title = models.CharField(max_length=65)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood = models.ForeignKey(Neighborhood, blank=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.description

class Business(models.Model):
    """Calss that defines the business model"""
    name = models.CharField(max_length=250,null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default =1)
    email_address = models.CharField(max_length=250,blank=True,null=True)
    neighborhood = models.ForeignKey(Neighborhood,null=True)

    def __str__(self):
        return self.name
    def save_business(self):
        self.save()
    @classmethod
    def delete_business_by_id(cls, id):
        business = cls.objects.filter(pk=id)
        business.delete()
    @classmethod
    def find_business(cls,id):
        business = cls.oblect.get(pk=id)
        return business
    @classmethod
    def update_business(cls,name,email_address,neighborhood):
        upd8 = cls.objects.filter(user=id)
        upd8.email_address = email_address
        upd8.neighborhood = neighborhood
        upd8.save()


    @classmethod
    def search_by_business_name(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

class Join(models.Model):
    user_id = models.OneToOneField(User)
    hood_id = models.ForeignKey(Neighborhood)

    def __str__(self):
        return self.user_id
class Location(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name