from django.urls import path
from.import views


urlpatterns = [
    path('',views.index,name='index'),
    path('user_signin/',views.user_sigin,name='user_signin'),
    path('email_verify/<str:token>/',views.email_verify,name='email_verify'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('add_post/',views.add_post,name='add_post'),
    path('edit_post/<int:id>/',views.edit_post,name='edit_post'),
    path('delete_post/<int:id>/',views.delete_post,name='delete_post'),
    path('view_post/<int:id>/',views.view_post,name='view_post'),
    path('user_posted/<str:id>/',views.user_posted,name='user_posted'),
    path('user_profile_edit/',views.user_profile_edit,name='edit_user'),
    path('change_password',views.change_password,name='change_password'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('password_verify/<str:id>/',views.password_verify,name='password_verify'),
    path('like_user/<int:id>/',views.like_user,name='like_user'),
    path('user_profile_views/',views.user_profile_views,name='user_profile_views'),
]