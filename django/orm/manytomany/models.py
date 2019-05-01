from django.db import models

# Create your models here.



# 병원에 오는 사람들을 기록하는 시스템을 만드려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떠한 관계로 표현할 수 있을까?

class Doctor(models.Model):
    name = models.TextField()
    

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    # class를 사용하면 Reservation에 다른 정보를 담을 수 있
    # doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    # Doctor : Patient = 1:N 
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
# Doctor : Reservation = 1:N -> Reservation = N*Doctor 
# Patient : Reservation = 1:M -> Reservation = M*Patient
# N*Doctor : M*Patient -> M:N = Doctor : Patient 
# Doctor : Patient = M : N
# class Reservation(models.Model):

#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete = models.CASCADE)    
# doctor1 = Doctor.objects.create(name='kim')
# doctor2 = Doctor.objects.create(name='kang')
# patient1 = Patient.objects.create(name='Tom')
# patient2 = Patient.objects.create(name='Anna')