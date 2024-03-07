from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    icon = models.ImageField(
        verbose_name="画像", upload_to="uploads", default="images/noimage.png"
    )
    
class Message(models.Model):
    message = models.CharField(max_length=1000)
    sender = models.ForeignKey(User, verbose_name='センダー', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, verbose_name='レシーバー', on_delete=models.CASCADE, related_name='receiver')
    pub_time = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    
    def __str__(self):
        return str(self.message) + '{} -> {}'.format(self.sender, self.receiver) + str(self.pub_time)