from django.db import models

# Create your models here.
class UpcomingEvents(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.title

class Events(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    imageUrl = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.name


class FocusTeam(models.Model):
    roles = [
        ('MAIN', 'MAIN'), ('DIRECTORS', 'DIRECTORS'), ('WEBMASTERS', 'WEBMASTERS'), ('LEADS', 'LEADS')
    ] 
    collegeId = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=300)
    groupName = models.CharField(max_length=50, choices=roles)
    def __str__(self) -> str:
        return f"{self.name} {self.collegeId}"

class Images(models.Model):
    imageName = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.imageName

class TechnologyClubs(models.Model):
    clubName = models.CharField(max_length=100)
    technology = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    mainPerson = models.CharField(max_length=50)
    theirRole = models.CharField(max_length=100)
    clubLogo = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.clubName