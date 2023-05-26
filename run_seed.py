import django
django.setup()

from students.seed import run

if __name__== '__main__':
    run()