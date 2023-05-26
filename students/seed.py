from django_seed import Seed    
from students.models import Student
import random


def run():
    seeder= Seed.seeder()
    genders=["H","F","NB","Tg","Tv","Q","GF"]
    seeder.add_entity(Student,20,{
        'nom': lambda x : seeder.faker.name(),
        'age': lambda x: random.randint(16,35),
        'genre': lambda x: genders[random.randint(0,6)],
        'email': lambda x : seeder.faker.ascii_free_email(), 
    })
    inserted_pks = seeder.execute()
    print(inserted_pks)