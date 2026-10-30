from django.contrib import admin

# Register your models here.
from web.models.user import UserProfile # 需要从软件包开始引用
from web.models.character import Character

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",) # 逗号千万不能删

@admin.register(Character)
class Character(admin.ModelAdmin):
    raw_id_fields = ("author",)

# 执行python manage.py makemigrations # 更新数据库
# 执行python manage.py migrate  # 数据库的更新同步到db.sqlite3