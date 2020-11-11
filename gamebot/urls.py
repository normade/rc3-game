from django.urls import path

from gamebot import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    # path("conversation/", views.get_conversation, name="get_conversation"),
    path("conversation/message/", views.post_message, name="post_message"),
]
