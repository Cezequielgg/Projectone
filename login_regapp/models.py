from django.db import models
import re	
import bcrypt

# Create your models here.
class Regvalidate(models.Manager):
    def basic_validation(request, postData):        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}   
        email_count = Userreg.objects.filter(email= postData['email'])       
        # add keys and values to errors dictionary for each invalid field
        if (postData['first_name']).isnumeric() == True:
            errors["first_name"] = "A Name cannot be numbers"
        if (postData['last_name']).isnumeric() == True:
            errors["last_name"] = "A Last name cannot be numbers"     

        if len(postData['first_name']) < 2:          
            errors["first_name"] = "Name should be at least 2 characters"
        if len(postData['last_name']) < 2:          
            errors["last_name"] = "Last name should be at least 2 characters"
        
        if postData['password'] != postData['password2']:
            errors["password"] = "Both password have to match"
        
        if not EMAIL_REGEX.match(postData['email']):        
            errors['email'] = ("Invalid email address!")          
        
        if email_count:
            errors['email_duplicate'] = ("email address is already in use")              
        
        return errors
    
    def basic_login(request, postData):
        user = Userreg.objects.filter(email = postData['email'])
        errors2 = {}  
        if len(user) == 0:
            errors2['username'] = ("This email adress hasnt been register")
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                errors2['password'] = ("wrong password")           
        
        return errors2


class Userreg(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255 )
    elo = models.IntegerField(default = 800) 
    password = models.CharField(max_length=255)
    region = models.CharField(max_length=255, default = "n/a")
    image = models.ImageField(upload_to = 'images/', default = "")
    
    objects = Regvalidate() 

