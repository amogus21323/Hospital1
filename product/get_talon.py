from datetime import date
from .models import Appointment
def get_appointments():

    appointments = Appointment.objects.all()
    appointments_with_talon = appointments.filter(STATUS_CHOICES='have')
    return appointments_with_talon