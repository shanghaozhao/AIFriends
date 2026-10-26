from django.contrib import admin

# Register your models here.
from web.models.user import UserProfile # 需要从软件包开始引用

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",) # 逗号千万不能删