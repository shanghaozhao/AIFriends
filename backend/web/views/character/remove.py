from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character


class RemoveCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            character_id = request.data['character_id']
            # 同样的这里的__user代表是author的属性 删除自己的
            Character.objects.filter(pk=character_id, author__user=request.user).delete()
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })