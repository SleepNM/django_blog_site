from django.urls import path
from .views import UserRegisterView, UserEditView, PassChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PassChangeView.as_view()),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page', CreateProfilePageView.as_view(), name='create_profile_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
