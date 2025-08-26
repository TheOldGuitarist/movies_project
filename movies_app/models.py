from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.DateField()
    gender = models.CharField(max_length=50)
    duration = models.DurationField()
    fk_director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
