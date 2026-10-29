from django.urls import path

from web.views.index import index
from web.views.user.account.getUserInfo import GetUserInfo
from web.views.user.account.login import LoginView
from web.views.user.account.logout import LogoutView
from web.views.user.account.refreshtoken import RefreshTokenView
from web.views.user.account.register import RegisterView

urlpatterns = [
    # 这里Django做URL匹配前，会先把请求路径的开头/剥掉再去做匹配。vue项目加上/
    path('api/user/account/login/', LoginView.as_view()),
    path('api/user/account/logout/', LogoutView.as_view()),
    path('api/user/account/register/', RegisterView.as_view()),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view()),
    path('api/user/account/get_user_info/', GetUserInfo.as_view()),
    path('', index, name='index')
]
