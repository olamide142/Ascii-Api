from django.db import models

# Create your models here.


class Account(models.Model):
    
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #username = models.
