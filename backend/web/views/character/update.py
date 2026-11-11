from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character
from web.views.utils.photo import remove_old_photo


class UpdateCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            character_id = request.data['character_id']
            # 首先 character_id会自动转化为整数
            # 从 Character 出发,跨到 User 的路径就是: 将. 转换为__
            # character.author                  → UserProfile 实例(通过外键 author)
            # character.author.user             → User 实例(通过 UserProfile 的 user 字段)
            # character.author.user.username    → 'alice'(通过 User 的 username 字段)
            character = Character.objects.get(id=character_id, author__user=request.user)
            name = request.data['name'].strip()
            profile = request.data['profile'].strip()[:100000]
            photo = request.FILES.get('photo', None)
            background_image = request.FILES.get('background_image', None)

            if not name:
                return Response({
                    'result': "名字不能为空"
                })
            if not profile:
                return Response({
                    'result': '角色介绍不能为空'
                })
            if photo:
                remove_old_photo(character.photo)
                character.photo = photo
            if background_image:
                remove_old_photo(character.background_image)
                character.background_image = background_image
            character.name = name
            character.profile = profile
            character.update_time = now()
            character.save()
            return Response({
                'result': 'success',
            })
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })
