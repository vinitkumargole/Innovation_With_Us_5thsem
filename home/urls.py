from django import views
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('details/', views.detail, name="detail"),
    path('login/', views.signin, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('learning/', views.learning, name="learning"),
    path('schemes/', views.schemes, name="schemes"),
    path('ideaform/', views.idea, name="idea"),
    path('idea', views.idea, name="idea1"), 
    path('chatbot/', views.chatbot, name="chatbot"),
    path('index', views.contact, name="contact"),
    path('contact/',views.contact1, name="contact1"),
]
