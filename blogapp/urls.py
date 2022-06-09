from django.urls import path, include
from .views import hello_home
from .views import hello_blog
from .views import post_detail

urlpatterns = [
    path('', hello_blog),
    path('blog/', hello_blog),
    path('post/<int:id>/', post_detail)
]

