from django.shortcuts import render
from clinicalsApp.models import Patient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class PatientListView(ListView):
    model = Patient


class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
