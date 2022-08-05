from django.shortcuts import render
from .models import Notes
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm
from .models import Notes

# Create your views here.

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/nnotes"
    template_name = "nnotes/notes_delete.html"

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = "/smart/nnotes"
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = "/smart/nnotes"
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "nnotes/notes_list.html"
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = "nnotes/notes-detail.html"