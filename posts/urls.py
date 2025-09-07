from django.urls import path
from .views import post_list  # или PostList, если используешь class-based view

urlpatterns = [
    path("", post_list, name="post_list"),  # или PostList.as_view()
]
