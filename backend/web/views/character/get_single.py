from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character


class GetSingleCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            character_id = request.query_params.get('character_id')
            # 这里请求的时候 前端还有这个Authorization: Bearer eyJhbGciOi...完整的JWT
            # 使用这个APIView和登陆确认之后后端会自动解析这个JWT并获取其中的id并且返回user
            # 从 Character 出发,跨到 User 的路径就是:character.author.user 将 . 转换为 __
            character = Character.objects.get(id=character_id, author__user=request.user)
            return Response({
                'result': 'success',
                'character': {
                    'id': character.id,
                    'name': character.name,
                    'profile': character.profile,
                    'photo': character.photo.url,
                    'background_image': character.background_image.url,
                }
            })
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })
