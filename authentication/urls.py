from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('login/patient/', views.patient_login, name='patient_login'),
    path('login/doctor/', views.doctor_login, name='doctor_login'),
    path('auth/callback/', views.auth_callback, name='auth_callback'),
    path('logout/', views.logout_view, name='logout'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/profile/complete/', views.doctor_profile_complete, name='doctor_profile_complete'),
    path('doctor/profile/edit/', views.doctor_profile_edit, name='doctor_profile_edit'),
    
    # Medical Records
    path('patient/medical-records/', views.medical_records_list, name='medical_records_list'),
    path('patient/medical-records/upload/', views.upload_medical_record, name='upload_medical_record'),
    path('patient/medical-records/<uuid:record_id>/', views.medical_record_detail, name='medical_record_detail'),
    path('patient/medical-records/<uuid:record_id>/delete/', views.delete_medical_record, name='delete_medical_record'),
]