from django.urls import path
from Posts.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', show_index_page, name="index"),
    path('post/<int:id>', show_post_page, name="post"),
    path('addPost/', show_add_post_page, name="add_post"),
    path('editPost/<int:id>', PostUpdateView.as_view(), name="edit_post"),
    path('deletePost/<int:id>', PostDeleteView.as_view(), name="delete_post"),
    path('logout/', LogoutViewPage.as_view(), name="logout"),
    path('login/', LoginViewPage.as_view(), name="login"),
    path('register/', RegisterViewPage.as_view(), name="register"),
    path('changePassword/', PasswordChangeViewPage.as_view(), name="change_password"),
    path('password_reset', password_reset_page, name="password_reset"),
]
