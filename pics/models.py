from django.db import models

# Create your models here.
class Image(models.Model):
    uploaded_image = models.ImageField( upload_to= 'uploads/')
    image_name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics

 # location
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location 

# category
class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

