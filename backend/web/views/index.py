from django.shortcuts import render

# 多行注释
# 浏览器拿到这个 HTML → 加载 index-xxx.js → Vue 应用挂载到 #app
# → vue-router 接管后续所有页面切换,之后用户点导航、进空间页都不再请求 Django,
# 只有 API 调用去 Django
def index(request):
    return render(request, 'index.html')