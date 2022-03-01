from django.contrib import admin
from django.urls import include, path
from todolist import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',include("todolist.urls")),
    path('account/',include("users_app.urls")),
    path("",todolist_views.index,name='index'),
    path("contact",todolist_views.contact,name='contact'),
    path("about",todolist_views.about,name='about'),
]
