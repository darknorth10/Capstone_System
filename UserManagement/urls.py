from django.urls import path
from . import views
urlpatterns = [
 path('', views.user_management, name="usermanagement"),
 path('edit_user/<int:id>', views.edit_user, name="edit_user"),
 path('edit_user/update_status/<int:id>', views.update_status_inactive, name="update_status"),
]