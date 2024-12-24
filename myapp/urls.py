from django.urls import path
from .views import hello
from .views import createpost

urlpatterns = [
    path("homepage/",hello,name="hello")
    ,path("createpost/",createpost,name="createpost")
]