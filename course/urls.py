from django.urls import path,include
from .views import CoursesDetailView,CoursesListView
app_name='course'
urlpatterns = [
    path('',CoursesListView.as_view(),name='list'),
    path('<slug>',CoursesDetailView.as_view(), name='detail')
]

  