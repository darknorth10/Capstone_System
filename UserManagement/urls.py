from django.urls import path
from . import views
urlpatterns = [
 path('', views.user_management, name="usermanagement"),
 path('edit_user/<int:id>', views.edit_user, name="edit_user"),
]