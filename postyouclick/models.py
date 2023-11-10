

# Create your models here
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin


# Create your models here.
class Signup_user(BaseUserManager):
    def create_user(self,email,username,password,**other_fields):
        if not email:
            raise ValueError('Enter an Email')
        if not username:
            raise ValueError('Enter an Username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password,**other_fields):
        user = self.create_user(
            username=username,
            email =email,
            password = password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user
        

class Newuser(AbstractBaseUser,PermissionsMixin):
    username    =              models.CharField(max_length=25)
    email       =              models.EmailField(unique=True)
    first_name  =              models.CharField(max_length=25)
    last_name   =              models.CharField(max_length=25)
    phone_number =             models.CharField(max_length=15)
    bio         =              models.ImageField(default='profile.jpg')
    token       =              models.CharField(max_length=50,blank=True,null=True)
    is_active   =              models.BooleanField(default=False)
    is_staff    =              models.BooleanField(default=False)
    is_superuser =             models.BooleanField(default=False)
    date_create  =             models.DateTimeField(auto_now_add=True)
    last_login   =             models.DateTimeField(auto_now=True) 
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    objects = Signup_user()


    @property
    def user(self):
        
        a=self.newimage_set.all()
        for i in a:
            print(a)
            return i




class NewImage(models.Model):
    name          = models.ForeignKey(Newuser,on_delete=models.CASCADE)
    post          = models.CharField(max_length=25)
    post_image    = models.ImageField()
    about_post    = models.TextField()
    date_of_post  = models.DateTimeField(auto_now_add=True)
    date_of_edit  = models.DateTimeField(auto_now=True)
    like          = models.ManyToManyField(Newuser,related_name='likes')
    
    @property
    def total_likes(self):
        return self.like.count()
    
    # @property
    # def total_user(self):
    #     for t in self.like.all()
            
    #         return self.like