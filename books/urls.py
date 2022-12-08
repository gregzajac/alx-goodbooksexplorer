from django.urls import path

from .views import books_list

app_name="books"
urlpatterns = [

    path("", books_list, name="list")
]