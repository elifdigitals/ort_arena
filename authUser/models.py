from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.db import models



class CustomUserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        username = self.model(email=email, username = username)

        username.set_password(password)
        username.save(using=self._db)

        return username
    
    def create_superuser(self, email, username, password):
        
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True, verbose_name='username')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='name')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='surname')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_set", 
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions_set",  
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",

    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username

    def __str__(self):
        return self.email
    
    def __str__(self):
        return self.username
