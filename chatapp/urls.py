from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conversation/<slug:obj>/', views.conversation,name='conversation')
    # path(r'^conversation/<str:obj>/',views.conversation,name='conversation')
]
