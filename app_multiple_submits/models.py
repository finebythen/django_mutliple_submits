from django.db import models


TYPES = (
    ('Benzin', 'Benzin'),
    ('Diesel', 'Diesel'),
    ('Elektro', 'Elektro'),
    ('Gas', 'Gas'),
)


class Car(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    type = models.CharField(max_length=10, null=False, blank=False, choices=TYPES, default=TYPES[0][1])

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
