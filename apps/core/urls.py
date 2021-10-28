from os import name
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Index.as_view(),name='index'),
    path('passport-info/', views.Passport.as_view(), name='passport-info'),
    path('passport-info-display/<str:pk>', views.PassportInfo.as_view(), name='passport-info-display'),
    path('members-list/', views.MembersList.as_view(), name='member-list'),
    path('download/list', views.download_members_list, name='download-list')
]