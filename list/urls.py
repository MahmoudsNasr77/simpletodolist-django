from django.urls import include, path
from .import views
app_name='job'
urlpatterns = [
    
    path('',views.todo_list,name='todo_list'),

    path('delete/<int:id>', views.delete, name='delete'),

]