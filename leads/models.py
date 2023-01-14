from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#    is_organiser = models.BooleanField(default=True)
#    is_agent = models.BooleanField(default=False)


# class UserProfile(models.Model):
#    user = models.OneToOneField(User,
#                                related_name="users",
#                                on_delete=models.CASCADE)

#    def __str__(self):
#        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # agent = models.ForeignKey("Agents", null=True, blank=True, on_delete=models.SET_NULL)
    # category = models.ForeignKey("Categories", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField(default="Text")
    date_added = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    profile_pics = models.ImageField(blank=True, null=True, upload_to='profile_pics/')
    special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
