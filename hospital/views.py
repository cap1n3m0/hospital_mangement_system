from django.shortcuts import render, redirect
from django.urls import reverse

# from django.shortcuts import reverse
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)

# from . models import (Hospitals, Services, DoctorServices, DoctorTimeSlots, Appointments)
from . models import (Services, DoctorServices, DoctorTimeSlots, Appointments)


# Create your views here.

#This is a method or function view that accepts a web request and returns back the index HTML page render
def home(request):
    return render(request, 'hospital/base.html')

def about(request):
    return render(request, 'hospital/about.html')

#-------------------------------------------------------------------------------------------------------------------------
# Services Views
'''
This is a class based view or a class 
that inherits its functionalities from django’s built in “CreateView” class. 
In this class we have to specify the model or database table the class will work with which is the “Services”,
the fields its to work with which are 'name' and 'description', the template that will render the data/form.
The class will also override its super class method “get_context_data”, what this method does, is that it allow us to get access to the data that will be passed to the template, 
before its sent to the template for rendering, the data is passed as a context object. After getting access to the context we add a new object variable with a value in it and return the context back.
We also override a super class method called “get_success_url” that will be used to return the URL page a user is to be redirected to after they successfully create a patient in the database.

'''

#-------------------------------------------------------------------------------------------------------------

class ServicesCreateView(CreateView):
    model = Services
    fields = ['name', 'description']
    # the template that will render the data/form.
    template_name = 'hospital/services_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add A New Service'
        return context
    def get_success_url(self) -> str:
        return reverse('services-list')
    
class ServicesListView(ListView):
    model = Services
    template_name = 'hospital/services_list.html'
    context_object_name = 'services'
    ordering = ['-pk']
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context
    
class ServicesDeleteView(DeleteView):
    model = Services
    success_url = '/'
    template_name = 'users/confirm_delete.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Service'
        service_name = Services.objects.get(pk=self.kwargs.get('pk')).name
        context['message'] = f'Are you sure you want to delete "{service_name}" ?'
        context['cancel_url'] = 'services-list'
        return context

class ServicesUpdateView(UpdateView):
    model = Services
    fields = ['name', 'description']
    template_name = 'hospital/services_detail.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Service Details'
        return context
    
    def get_success_url(self):
        return reverse('services-list')

#------------------------------------------------------------------------------------------------------------------------
# DoctorServices Views
class DoctorServicesCreateView(CreateView):
    model = DoctorServices
    fields = ['service', 'doctor']
    template_name = 'hospital/doctor_services_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add A New Doctor And Service'
        return context
    def get_success_url(self) -> str:
        return reverse('doctor-services-list')

class DoctorServicesListView(ListView):
    model = DoctorServices
    template_name = 'hospital/doctor_services_list.html'
    context_object_name = 'doctor_services'
    ordering = ['-pk']
    paginate_by = 10


    
class DoctorServicesDeleteView(DeleteView):
    model = DoctorServices
    template_name = 'users/confirm_delete.html'

 
    def get_success_url(self):
        return reverse('doctor-services-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Doctor Service'
        doctor_service = DoctorServices.objects.get(pk=self.kwargs.get('pk'))
        context['message'] = f'Are you sure you want to delete "{doctor_service}" ?'
        context['cancel_url'] = 'doctor-services-list'
        return context

class DoctorServicesUpdateView(UpdateView):
    model = DoctorServices
    fields = ['service', 'doctor']
    template_name = 'hospital/doctor_services_detail.html'

    
    def get_success_url(self) -> str:
        return reverse('doctor-services-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Doctor Service Details'
        return context 


#--------------------------------------------------------------------------------------------------------------------------
# DoctorTimeSlots Views
#  
class DoctorTimeSlotsCreateView(CreateView):
    model = DoctorTimeSlots
    fields = ['doctor_service', 'date', 'start_time', 'end_time']
    template_name = 'hospital/doctor_time_slots_detail.html'
    def get_success_url(self) -> str:
        return reverse('doctor-time-slots-list')
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['table_title'] = 'Add A New Doctor Time Slot'
        return context

class DoctorTimeSlotsListView(ListView):
    model = DoctorTimeSlots
    template_name = 'hospital/doctor_time_slots_list.html'
    context_object_name = 'doctor_time_slots'
    ordering = ['-pk']
    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class DoctorTimeSlotsDeleteView(DeleteView):
    model = DoctorTimeSlots
    # success_url = '/'
    template_name = 'users/confirm_delete.html'
    def get_success_url(self) -> str:
        # redirect user back to the page displaying a list of doctor time slots
        return reverse('doctor-time-slots-list')
 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete Doctor's Time Slot"
        doctor_time_slot = DoctorTimeSlots.objects.get(pk=self.kwargs.get('pk'))
        context['message'] = f'Are you sure you want to delete the following Doctor Time Slot: "{doctor_time_slot}" ?'
        context['cancel_url'] = 'doctor-time-slots-list'
        return context


class DoctorTimeSlotsUpdateView(UpdateView):
    model = DoctorTimeSlots
    fields = ['doctor_service', 'start_date', 'end_date']

    template_name = 'hospital/doctor_time_slots_detail.html'
    def get_success_url(self) -> str:
        return reverse('doctor-time-slots-list') 
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = "Update Doctor's Time Slot Details"
        return context

#--------------------------------------------------------------------------------------------------------------------------
# Appointments

class AppointmentsCreateView(CreateView):
    model = Appointments
    fields = ['doctor_time_slots', 'patient','booking_code']
    template_name = 'hospital/appointments_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add A New Appointment'
        return context
    def get_success_url(self) -> str:
        return reverse('appointments-list')
    
class AppointmentsListView(ListView):
    model = Appointments
    template_name = 'hospital/appointments_list.html'
    context_object_name = 'appointments'
    ordering = ['-pk']
    paginate_by = 10


    
class AppointmentsDeleteView(DeleteView):
    model = Appointments
    template_name = 'users/confirm_delete.html'
    
    def get_success_url(self) -> str:
        return reverse('appointments-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Appointment'
        patient_appointment= Appointments.objects.get(pk=self.kwargs.get('pk'))
        context['message'] = f"Are you sure you want to cancel {patient_appointment.patient}'s appointment on {patient_appointment.doctor_time_slots.date} at {patient_appointment.doctor_time_slots.start_time}?"
        context['cancel_url'] = 'appointments-list'
        return context

class AppointmentsUpdateView(UpdateView):
    model = Appointments
    fields = ['doctor_time_slots', 'patient','booking_code']

    template_name = 'hospital/appointments_detail.html'
    def get_success_url(self):
        return reverse('appointments-list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Appointment Details'
        return context
#----------------------------------------------------------------------------------------------------------------------------


# class HospitalsCreateView(CreateView):
#     model = Hospitals
#     fields = ['name', 'services']
#     template_name = 'hospital/hospitals_detail.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['table_title'] = 'Add A New Hospital'
#         return context
    
#     def get_success_url(self) -> str:
#         return reverse('hospitals-list')

# class HospitalsListView(ListView):
#     model = Hospitals
#     template_name = 'hospital/hospitals_list.html'
#     context_object_name = 'hospitals'
#     ordering = ['-pk']
#     paginate_by = 10



 

# class HospitalsDeleteView(DeleteView):
#     model = Hospitals
#     success_url = '/'
#     template_name = 'users/confirm_delete.html'
   
#     def get_context_data(self, **kwargs):
#             context = super().get_context_data(**kwargs)
#             context['title'] = 'Delete Hospital'
#             hospital_name = Hospitals.objects.get(pk=self.kwargs.get('pk')).name
#             context['message'] = f'Are you sure you want to delete "{hospital_name}" ?'
#             context['cancel_url'] = 'hospitals-list'
#             return context

# class HospitalsUpdateView(UpdateView):
#     model = Hospitals
#     fields = ['name', 'services']
#     template_name = 'hospital/hospitals_detail.html'
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         context['table_title'] = 'Update Hospital Details'
#         return context
    
#     def get_success_url(self):
#         return reverse('hospitals-list')