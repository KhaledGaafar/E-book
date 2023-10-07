from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    noOFitems=models.IntegerField()
    description=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    instock=models.CharField(max_length=100,default="avalible")
    image=models.ImageField(upload_to='books/images/', null=True, blank=True)
    borrow=models.IntegerField()
    
    
    

    def __str__(self) :
        return self.name
    
    
    @classmethod
    def get_all_products(cls):
        return  cls.objects.all()

    @classmethod
    def get_specific_book(cls, id):
        return  cls.objects.get(id=id)

    def get_image_url(self):
        return f'/media/{self.image}'
    
    
    def get_show_url(self):
        return reverse('show-books',args=[self.id])

    def get_delete_url(self):
        return reverse('delete',args=[self.id])
    def get_update_url(self):
        return reverse('update',args=[self.id])

    def get_borrow_url(self):
        return reverse('borrow',args=[self.id])
    

   
