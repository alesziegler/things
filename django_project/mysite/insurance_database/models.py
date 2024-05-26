from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Customer(models.Model):
  given_name = models.CharField(max_length=200)
  surname = models.CharField(max_length=200)
  age = models.IntegerField()
  contact = models.CharField(max_length=20)
    
  def __str__(self):
    return f"{self.given_name}, {self.surname}, {self.age}, {self.contact}"
  

class UserManager(BaseUserManager):
    
    def create_user(self, email, password):
        print(self.model)
        if email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
            return user
        
        
class User(AbstractBaseUser):

    email = models.EmailField(max_length=300, unique=True)
    """
    below potentially problematic change from Django tutorial, 
    where default is False.
    Reason: I do not want users unable to change data(i.e. simplification).
    """
    is_admin = models.BooleanField(default=True) 

    class Meta:
        verbose_name = "uživatel"
        verbose_name_plural = "uživatelé"

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "email: {}".format(self.email)

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True