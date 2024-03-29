from django.urls import path

from preparation_project_web_basics.web import views

urlpatterns = [
    path("", views.home_page, name="home page"),
    path("album/add/", views.add_album, name="add album page"),
    path("album/details/<int:id>/", views.album_details, name="album details page"),
    path("album/edit/<int:id>/", views.album_edit, name="edit album page"),
    path("album/delete/<int:id>/", views.album_delete, name="delete album page"),

    path("profile/details/", views.profile_details, name="profile details page"),
    path("profile/delete/", views.profile_delete, name="delete profile page"),
]
