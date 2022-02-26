from django.shortcuts import render, redirect
from clinicalsApp.models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm


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


def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldata_form.html', {"form": form, 'patient': patient})


def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    response_data = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            height_weight = eachEntry.componentValue.split('/')
            height_in_meters = float(height_weight[0]) / 100
            body_mass_index = (float(height_weight[1])) / (height_in_meters * height_in_meters)
            bmi_entry = ClinicalData()
            bmi_entry.componentName = 'BMI'
            bmi_entry.componentValue = body_mass_index
            response_data.append(bmi_entry)
        response_data.append(eachEntry)
    return render(request, 'clinicalsApp/generateReport.html', {"data": response_data})
