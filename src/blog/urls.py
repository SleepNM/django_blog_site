from django.urls import path
# from . import views
from .views import HomeView, AricleDetaliView, AddPostView, UpdatePostView,\
                    DeletePostView, AddCategoryView, category_view,\
                    category_list_view, like_view, AddCommentView

urlpatterns = [
    # path('', views.home, name="home"),
    path(
        '',
        HomeView.as_view(),
        name="home"
        ),
    path(
        'article/<int:pk>',
        AricleDetaliView.as_view(),
        name='article_detail'
        ),
    path(
        'add_post/',
        AddPostView.as_view(),
        name='add_post'
        ),
    path(
        'add_category/',
        AddCategoryView.as_view(),
        name='add_category'
        ),
    path(
        'article/edit/<int:pk>',
        UpdatePostView.as_view(),
        name='update_post'
        ),
    path(
        'article/<int:pk>/remove',
        DeletePostView.as_view(),
        name='delete_post'
        ),
    path(
        'category/<str:slug>/',
        category_view,
        name="category"
        ),
    path(
        'category-list/',
        category_list_view,
        name="category-list"
        ),
    path(
        'like/<int:pk>',
        like_view,
        name='like_post'
        ),
    path(
        'article/<int:pk>/comment/',
        AddCommentView.as_view(),
        name='add_comment'
        ),
]
