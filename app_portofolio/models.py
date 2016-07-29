from django.db import models

class contato(models.Model):
    first_name  = models.CharField(max_length=150)
    last_name   = models.CharField(max_length=150)
    email       = models.EmailField()
    phone       = models.CharField(max_length=150)
    message_text = models.TextField()
    data = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.email


