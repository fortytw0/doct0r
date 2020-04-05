from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [

    path("" , views.index , name="index_view") , 
    path("todo" , views.article_view , name = "article_view")


]