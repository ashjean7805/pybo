from django.urls import path
from . import views

## 네임스페이스 관리용
app_name = 'pybo'


urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.detail, name = 'detail'),
    path('answer/create/<int:question_id>', views.answer_create, name = 'answer_create'),
]