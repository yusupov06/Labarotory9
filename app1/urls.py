from django.urls import path
from .views import *

urlpatterns = [
    path('', Post_view.as_view(), name='Post_view'),
    path('post/<int:pk>', Post_detail.as_view(), name='detail_page'),
    path('post/new', Create_post.as_view(), name='Create_view' ),
    path('<int:pk>/edit', Edit_post.as_view(), name='edit_page'),
    path('<int:pk>/delete', Delete_post.as_view(), name='delete_page'),
    path('logout', Logout_view, name='logout')
]