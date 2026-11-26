import json

from django.http import StreamingHttpResponse
from langchain_core.messages import HumanMessage, BaseMessage, BaseMessageChunk, AIMessage
from rest_framework.renderers import BaseRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.friend import Friend
from web.views.friend.message.chat.graph import ChatGraph

# 让他支持这个SSE 流式返回
class SSERenderer(BaseRenderer):
    media_type = 'text/event-stream'
    format = 'txt'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data

class MessageChatAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (SSERenderer,)
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
            "messages": [HumanMessage(content=message)]
        }

        # 使用这个stream_model就可以实现这里的流式返回了，但是返回的东西需要使用这个事件来使用
        def event_stream():
            full_usage = {}
            for msg, metadata in app.stream(inputs,stream_mode="messages"):
                if isinstance(msg, AIMessage): # 代码这写的是 BaseMessageChunk
                    if msg.content:
                        yield f"data: {json.dumps({'content' : msg.content},ensure_ascii=False)}\n\n"
                    if hasattr(msg, "usage_metadata") and msg.usage_metadata:
                        full_usage = msg.usage_metadata

            yield 'data: [DONE]\n\n'
            print(full_usage)

        # 这里设置为流式响应
        response = StreamingHttpResponse(event_stream(), content_type="text/event-stream")
        response['Cache-Control'] = 'no-cache'
        return response