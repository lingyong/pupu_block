from django.db import models

# Create your models here.
class Block(models.Model):
    time = models.IntegerField(unique=True)
    block_hash = models.CharField(max_length=64)

    def __str__(self):
        return 'hash: {}, time: {}'.format(self.block_hash, self.time)
