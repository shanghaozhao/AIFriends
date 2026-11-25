from langchain_core.messages import HumanMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.friend import Friend
from web.views.friend.message.chat.graph import ChatGraph


class MessageChatAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        friend_id = request.data.get('friend_id')
        message = request.data.get('message').strip()
        if not message:
            return Response({'error': 'Message is required'})
        friends = Friend.objects.filter(id=friend_id, me__user=request.user)
        if not friends.exists():
            return Response({'error': 'Friend not found'})

        friend = friends.first()

        app = ChatGraph.create_app()
        inputs = {
            "message": HumanMessage(content=message)
        }

        res = app.invoke(inputs)
        print(res["message"][-1].content)

        return Response({
            "result":"success"
        })
