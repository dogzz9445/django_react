from django.urls import path
from backend import views
from backend.views import PostListView

urlpatterns = [
    #path('', views.index, name='index'),
    path(r'^post/$', PostListView.as_view(), name='post'),
]