from django.db import models
from django.utils.text import slugify

JOB_OPTION = [
    ('F','Full time'),
    ('P','Part time'),
]
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=75)
    designation = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name','designation','company'],name='Author_unique_combination'
            )
        ]
    def __str__(self) -> str:
        return {'Author':self.name,'Designation':self.designation,'Company':self.company}

class JobLocation(models.Model):
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=75)
    country = models.CharField(max_length=80)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city','state','country'],name='Job_location_unique_combination'
            )
        ]
    def __str__(self) -> str:
        return f'{self.city}, {self.state}, {self.country}'

class Skills(models.Model):
    class Meta:
        verbose_name_plural = "Skills"
    skill = models.CharField(max_length=200,unique=True) 

    def __str__(self) -> str:
        return self.skill

class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    salary = models.IntegerField()
    job_location = models.ManyToManyField(JobLocation)
    date_posted = models.DateField(auto_now_add=True)
    skills = models.ManyToManyField(Skills)
    job_option = models.CharField(max_length=1,choices=JOB_OPTION,default='F')
    expiry = models.DateField(null=True)

    slug = models.SlugField(max_length=40,null=True,unique=True)

    def job_location_city_names(self):
        return ', '.join([c.city for c in self.job_location.all()])
    job_location_city_names.short_description = "City"

    def job_skills(self):
        return [s.skill for s in self.skills.all()]
    job_skills.short_description = "Skills"


    def save(self,*args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost,self).save(*args,**kwargs)
    
    def __str__(self):
        return f'{self.title} with salary of {self.salary}'

    
