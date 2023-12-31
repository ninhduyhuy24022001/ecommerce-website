from django.db import models
from django.core.files import File
from django.contrib.auth.models import User

from io import BytesIO
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to="category_image", blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail_image', blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/300x200.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img = img.resize(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=2000)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="product_image", blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail_image', blank=True, null=True)

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.name
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/300x200.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img = img.resize(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "JPEG", quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    
    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating
        
        if reviews_total > 0:
            return reviews_total / self.reviews.count()
        
        return 0
class Review(models.Model):
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)