from django.db import models

from django.db import models

class CartItem(models.Model):
    excel = models.FileField(upload_to='excel')