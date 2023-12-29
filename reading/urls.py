from django.urls import path
from .views import ReadingList, ReadingDetail, ReadingCreate, ReadingUpdate, ReadingDelete # 追加

urlpatterns = [
    path("", ReadingList.as_view(), name="list"),
    path("detail/<int:pk>", ReadingDetail.as_view(), name="detail"),
    path("create/", ReadingCreate.as_view(), name="create"),
    path("update/<int:pk>", ReadingUpdate.as_view(), name="update"),
    path("delete/<int:pk>", ReadingDelete.as_view(), name="delete"), # 追加
]