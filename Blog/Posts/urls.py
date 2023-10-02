from django.urls import path
from Posts.views import *

urlpatterns = [
    path('', show_index_page, name="index"),
    path('post/<int:id>', show_post_page, name="post"),
    path('addPost/', show_add_post_page, name="add_post"),
    path('logout/', LogoutViewPage.as_view(), name="logout"),
    path('login/', LoginViewPage.as_view(), name="login"),
    path('register/', RegisterViewPage.as_view(), name="register"),
]
