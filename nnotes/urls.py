from django.urls import path
from . import views

urlpatterns = [
    path('nnotes', views.NotesListView.as_view(), name="nnotes.list"),
    path('nnotes/<int:pk>', views.NotesDetailView.as_view(), name="nnotes.detail"),
    path('nnotes/new', views.NotesCreateView.as_view(), name="nnotes.new"),
    path('nnotes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="nnotes.update"),
    path('nnotes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="nnotes.delete"),

]