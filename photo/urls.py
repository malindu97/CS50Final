from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("signin", views.signin, name="signin"),
    path("logout", views.logout_view, name="logout"),
    path("home/upload", views.uploadImage, name="upload"),
    path("home/mygallery/<str:user>", views.mygallery, name="mygallery"),
    path("home/mygallery/<str:user>/<int:id>", views.viewimage, name="viewimage"),
    path("home/<str:user>/<int:id>", views.viewimageother, name="viewimageother"),
    path("home/<str:user>/<int:id>/voted", views.voteimage, name="voteimage"),
    path("home/mygallery/<str:user>/<int:id>/delete", views.deleteImage, name="deleteImage"),
    path("home/mygallery/<str:user>/<int:id>/edit", views.editimage, name="editimage"),
    path("home/mygallery/<str:user>/<int:id>/updated", views.updateimage, name="updateimage")
]

