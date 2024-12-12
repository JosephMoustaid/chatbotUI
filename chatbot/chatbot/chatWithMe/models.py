from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime 


# Create your models here.
class User(models.Model):
    firstname = models.fields.CharField(max_length = 100, null = False)
    lastname = models.fields.CharField(max_length = 100, null = False)
    birthdate = models.DateTimeField( null = False ,
        validators=[
            MinValueValidator(limit_value=datetime.datetime(1950, 1, 1)),
            MaxValueValidator(limit_value=datetime.datetime(2000, 12, 31)),
        ]
    )
    class Sex(models.TextChoices):
        male = "m"
        female = "f"
    sex = models.fields.CharField(choices= Sex.choices , null = False)
    email = models.fields.EmailField(max_length = 254 , unique = True ,null = False)
    password = models.fields.CharField(max_length = 100 , null = False)

    def __str__(self) :
        return f"{this.firstname} {this.lastname}"

    def chat(self, prompt):
        answer =""
        return answer

class Chat(models.Model):
    class Type(models.TextChoices):
        PROMPT = "p", "Prompt"
        ANSWER = "a", "Answer"

    type = models.CharField(max_length=1, choices=Type.choices, null=False)
    message = models.CharField(max_length=1500)
    date = models.DateField(auto_now_add=True)  
    time = models.TimeField(auto_now_add=True) 
    feed = models.ForeignKey(Feed , null= False , on_delete = models.CASCADE)
    def __str__(self):
        return f"{self.get_type_display()} - {self.date} {self.time}"

class Feed(models.Model):
    date = models.DateField(auto_now_add=True)  