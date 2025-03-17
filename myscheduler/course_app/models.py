from django.db import models
from django.utils.text import slugify

# Create your models here.

class Course(models.Model):
    CATEGORY = (("Math", "MATH"),
                ("Computer_Science", "CPTS"),
                ("Biology", "BIO"),
                ("Physics", "PHYS"),
                ("Chemistry", "CHEM"),
                ("History", "HIST")
                )
    name = models.CharField(max_length= 20, null = False)
    id_number = models.CharField(max_length = 3, primary_key=True)
    slug = models.SlugField(blank = True, null = True)
    image = models.ImageField(upload_to="img")
    category = models.CharField(max_length=20,choices=CATEGORY)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            counter = 1
            if Course.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{counter}'
                counter +=1
            self.slug = unique_slug

        super().save(*args, **kwargs)
