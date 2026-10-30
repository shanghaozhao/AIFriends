from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.user import UserProfile
from web.models.character import Character

class CreateCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)
            character_name = request.data.get('character_name').strip()
            character_profile = request.data.get('character_profile').strip()[:100000]
            character_photo = request.data.get('character_photo',None)
            character_background_image = request.data.get('character_background_image',None)

            if not character_name:
                return Response({'result': "角色名不能为空"})
            if not character_profile:
                return Response({'result': "角色简介不能为空"})
            if not character_photo:
                return Response({'result': "角色图片不能为空"})
            if not character_background_image:
                return Response({'result': "角色背景图片不能为空"})
            Character.objects.create(
                author=user_profile,
                name=character_name,
                profile=character_profile,
                photo=character_photo,
                background_image=character_background_image
            )
            return Response({
                'result': "success",
            })
        except:
            return Response({'result': "系统异常，请稍后重试"})