from django.db import models
from django.utils.text import slugify 



# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        # proxy = True
    

class Category(BaseModel):
    title = models.CharField(max_length=255,unique=True)
    image = models.ImageField(upload_to='category/images/')
    slug = models.SlugField(null=True,blank=True)
    
    
    def save(self,*args,**kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.title
    
    
class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name

    
    
    
    class Meta:
        verbose_name_plural = 'products'
        verbose_name = 'product'
        
        
        
class Image(BaseModel):
    image = models.ImageField(upload_to='product/images/')
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images',
                                null=True,
                                blank=True
                                )
    is_primary = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.product} - {self.image.url}'
    
    
    
    
    
class AttributeKey(BaseModel):
    key_name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.key_name
    
    
   
class AttributeValue(BaseModel):
    value_name = models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return self.value_name
    
    

    
class Attribute(BaseModel):
    attribute_key = models.ForeignKey(AttributeKey,on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(AttributeValue,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.product.name} - {self.attribute_key.key_name} - {self.attribute_value.value_name}'





# 2 , 10,10_000
# 3,12,5