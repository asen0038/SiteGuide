from django.urls import path

from vehicles.views import ListAll, Create, Update, Delete

urlpatterns = [
    path('', ListAll.as_view()),
    path('create', Create.as_view()),
    path('update/<id>', Update.as_view()),
    path('delete/<id>', Delete.as_view()),
]
