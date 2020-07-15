from django.db import models

# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(primary_key=True, db_index=True, max_length=80)
    definition = models.CharField(max_length=480, null=False)

    def __str__(self):
        return(self.word)
