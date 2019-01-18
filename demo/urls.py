from django.urls import  path
from demo import views

urlpatterns = [
    path('', views.show_subject, name='demo'),
    path('subject/<int:no>', views.show_teachers),
    path('good/<int:no>/', views.make_comment),
    path('bad/<int:no>/', views.make_comment),
]