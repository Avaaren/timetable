from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetTimetableView.as_view(), name='general_timetable'),
    path('<slug:group>/', views.GroupTimetableView.as_view(), name='group_timetable'),
    path('add/', views.AddTimetableView.as_view(), name='add_timetable'),
    path('<int:pk>/edit/', views.EditTimetableView.as_view(), name='edit_timetable'),
    path('<int:pk>/delete/', views.DeleteTimetableView.as_view(), name='edit_timetable'),

]