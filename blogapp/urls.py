from django.urls import path, include
from .views import hello_home
from .views import hello_blog

urlpatterns = [
    path('', hello_blog),
    path('blog/', hello_blog),
]

