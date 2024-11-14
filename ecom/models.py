from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


# models.py

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Boys', 'Boys'),
        ('Girls', 'Girls'),
        ('Kids', 'Kids'),
        ('Accessories', 'Accessories'),
    ]


    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=40)
    category = models.CharField(max_length=11, choices=CATEGORY_CHOICES, default='Men')

    def __str__(self):
        return self.name

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            return total_rating / len(reviews)
        return None


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"


class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
from django.db import models

from django.db import models

class Designer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DesignerImage(models.Model):
    designer = models.ForeignKey(Designer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='designer_images/')

    def __str__(self):
        return f"Image for {self.designer.name}"

