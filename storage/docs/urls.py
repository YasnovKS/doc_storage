from django.urls import path
from . import views

app_name = 'docs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CreateDocument.as_view(), name='doc_create'),
    path(
        'document/<pk>/', views.DocumentDetail.as_view(),
        name='doc_detail'
    ),
    path(
        'document/<pk>/edit/', views.edit_document,
        name='doc_edit'
    ),
    path('document/<pk>/delete/', views.delete_document,
         name='doc_delete',
         ),
]
