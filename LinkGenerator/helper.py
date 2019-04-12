from django.utils.text import slugify
import random


def random_slugger():
    return slugify([random.randint(0, 900), random.randint(10, 20), random.randint(5, 80)])