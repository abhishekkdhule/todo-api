from django.urls import path
from . import views
urlpatterns=[
    path('checklists/',views.CheckListsAPI.as_view(),name="checklists"),
    path('checklist/<int:pk>/',views.CheckListAPI.as_view(),name="checklist"),
    path('checklistitem/create/',views.checkListItemCreateAPI.as_view(),name="checklistitemcreate"),
    path('checklistitem/<int:pk>/',views.checkListItemAPI.as_view(),name="checklistitemupdate"),
]