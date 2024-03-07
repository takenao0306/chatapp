from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path("login/", views.Login.as_view(), name="login"),
    path('friends/', views.friends, name='friends'),
    path('talk_room/<int:user_id>', views.talk_room, name='talk_room'),
    path('setting/', views.setting, name='setting'),
    path('setting/change_username/', views.change_username, name='change_username'),
    path('setting/change_username_done/', views.change_username_done, name='change_username_done'),
    path('setting/change_mail/', views.change_mail, name='change_mail'),
    path('setting/change_mail_done/', views.change_mail_done, name='change_mail_done'),
    path('setting/change_icon/', views.change_icon, name='change_icon'),
    path('setting/change_icon_done/', views.change_icon_done, name='change_icon_done'),
    path('setting/change_password/', views.ChangePassword.as_view(), name='change_password'),
    path('setting/change_password_done/', views.ChangePasswordDone.as_view(), name='change_password_done'),
    path('logout/', LogoutView.as_view(), name='logout'),
]