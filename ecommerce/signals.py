from .models import Product
from django.db.models.signals import post_save , pre_save , pre_delete
from django.dispatch import receiver
from django.conf import settings
import os 
import json

@receiver(post_save, sender=Product)
def send_massage(sender ,  created , instance , **kwargs):
    if created:
        print("Product Created")
        print(f"Product Name : {instance.name}")
        print(f"Product Price : {instance.price}")
    

@receiver(pre_delete, sender=Product)
def save_product_before_delete(sender, instance, **kwargs):
    backup_dir = os.path.join(settings.MEDIA_ROOT , 'backups')
    os.makedirs(backup_dir , exist_ok=True)
    backup_path = os.path.join(backup_dir , f'product_{instance.id}.json')



    data = {
        'id' : instance.id,
        'name' : instance.name,
        'price' : str(instance.price) ,
        'description' : instance.description,
    }

    with open(backup_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4 , default=str)