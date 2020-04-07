from django.db import models

class Memo(models.Model):
    memotext = models.TextField()

    def __str__(self):
        return self.memotext