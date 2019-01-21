from django.urls import path

from goods import views


urlpatterns = [
    # 首页
    path('index/', views.index, name='index'),
    path('list/<int:id>/', views.list, name='list'),
    # 详情
    path('detail/<int:id>/', views.detail, name='detail'),
]
