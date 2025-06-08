from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.signup),
    path('signup/', views.signup),
    path("login/", views.loginn),
    path('todopage/', views.todo),
    path('delete_todo/<int:srno>', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('signout/', views.signout, name='signout'),
]
