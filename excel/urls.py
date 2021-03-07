from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name="login"),
    path('file_view/<str:username>', views.file_view, name='file_view'),
    path('logout/', views.logout_view, name='logout'),
    path('update_data/', views.update, name='update'),
    path('ajax_example/', views.likePost, name='likePost'),
    path('get_item/', views.search_item, name='likePost'),
    
]
