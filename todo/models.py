from django.contrib.auth.models import User
from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=50) #제목
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField() # 설명
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


