from django.urls import path
from . views import Article_detail,Article_list
urlpatterns = [
    path('article/',Article_list),
    path('detail/<int:pk>/',Article_detail)
]
