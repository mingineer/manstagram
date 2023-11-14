from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),    # 경로, view, 라우팅 이름

]
