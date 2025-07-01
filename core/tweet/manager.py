from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self,email,username,interest=None,password=None,**extra_fields):
        if not email:
            raise ValueError ("Email is required")
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,interest=interest,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email=email,username=username,password=password,**extra_fields)
