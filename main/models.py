from django.db import models

class Users(models.Model):
    name = models.CharField('Имя',max_length=50,default='anon')
    message = models.TextField('Сообщение',max_length=1000)
    room = models.CharField('Комната',max_length=1,default='0')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
