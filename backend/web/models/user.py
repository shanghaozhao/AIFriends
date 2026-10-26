import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now,localtime

def photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4().hex[10]}.{ext}'
    return f'users/photos/{instance.user_id}_{filename}'


# 这就定义了一个数据库表
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 虽然是创建了一个对象user 同时会创建一个外键字段名+_id 即user_id
    photo = models.ImageField(default='user/photos/default.jpg', upload_to=photo_upload_path)
    profile = models.TextField(default='谢谢你的关注', max_length=500)
    create_time = models.DateTimeField(default=now)
    update_time = models.DateTimeField(default=now)

    # 返回的是你对应的一个键，去索引这个userProfile{id, photo, profile, create_time, update_time}
    def __str__(self):
        return f'{self.user.username} - {localtime(self.create_time).strftime("%Y-%m-%d %H:%M:%S")}'
