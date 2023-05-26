from django.db import models
from django.core.validators import MaxLengthValidator,MaxValueValidator,MinLengthValidator, MinValueValidator
# Create your models here.
class Student(models.Model):
    class Genre(models.TextChoices):
        Homme = 'H'
        Femme = "F"
        Non_Binaire = "NB"
        Transgenre = "Tg"
        Gender_Fluid = "GF"
        Queer = "Q"
        Travesti = "Tv"
    nom=models.CharField(max_length=50,
        validators=[MinLengthValidator(3),MaxLengthValidator(50)]
    )
    genre=models.CharField(choices=Genre.choices,max_length=2)
    email=models.EmailField()
    age=models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(35)]
    )