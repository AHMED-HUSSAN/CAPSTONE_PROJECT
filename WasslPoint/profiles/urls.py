# WasslPoint/profiles/urls.py
from django.urls import path
from . import views
app_name = "profiles"
urlpatterns = [
    path('profile/',views.profile_view,name='profile_view'),
    path('profile/<int:user_id>/',views.profile_view,name='profile_view_admin'), # Changed path arg to int
    path('company_profile/',views.company_profile_view,name='company_profile_view'),
    path('company_profile/edit-pending/',views.add_edit_company_info_company,name='add_edit_company_info_company'),
    path('company_profile/<int:user_id>/',views.company_profile_view,name='company_profile_view_admin'), # Changed path arg to int
    path('company_profile/<int:user_id>/add_/',views.add_edit_company_info,name='add_edit_company_info'), # Corrected path typo (_add vs add_)
    path('company_profile/add_contact/',views.add_edit_contact_person,name='add_edit_contact_person'), # Added slash? Check consistency
    path('company_profile/add_moreinfo/',views.add_edit_moreinfo_company,name='add_edit_moreinfo_company'),
    path('company_profile/edit_logo/',views.edit_logo,name='edit_logo'),
    path('company_profile/<int:user_id>/edit_logo/',views.edit_logo,name='edit_logo_admin'), # Added int converter
    path('company_profile/<int:user_id>/add_contact/',views.add_edit_contact_person,name='add_edit_contact_person_admin'), # Added int converter
    path('company_profile/<int:user_id>/add_moreinfo/',views.add_edit_moreinfo_company,name='add_edit_moreinfo_company_admin'), # Added int converter
    path('delate_exp/<int:exp_id>/',views.delate_exp,name='delate_exp'), # Added int converter
    path('<int:user_id>/delate_exp/<int:exp_id>/',views.delate_exp,name='delate_exp_admin'), # Added int converter
    path('edit_exp/<int:exp_id>/',views.edit_exp,name='edit_exp'), # Added int converter
    path('<int:user_id>/edit_exp/<int:exp_id>/',views.edit_exp,name='edit_exp_admin'), # Added int converter
    path('delate_skill/<int:skill_id>/',views.delate_skill,name='delate_skill'), # Added int converter
    path('<int:user_id>/delate_skill/<int:skill_id>/',views.delate_skill,name='delate_skill_admin'), # Added int converter
    path('edit_skill/<int:skill_id>/',views.edit_skill,name='edit_skill'), # Added int converter
    path('<int:user_id>/edit_skill/<int:skill_id>/',views.edit_skill,name='edit_skill_admin'), # Added int converter
    path('delate_lan/<int:lan_id>/',views.delate_language,name='delate_language'), # Added int converter
    path('<int:user_id>/delate_lan/<int:lan_id>/',views.delate_language,name='delate_language_admin'), # Added int converter
    path('edit_lan/<int:lan_id>/',views.edit_language,name='edit_language'), # Added int converter
    path('<int:user_id>/edit_lan/<int:lan_id>/',views.edit_language,name='edit_language_admin'), # Added int converter
    path('delate_edu/<int:edu_id>/',views.delate_edu,name='delate_edu'), # Added int converter
    path('<int:user_id>/delate_edu/<int:edu_id>/',views.delate_edu,name='delate_edu_admin'), # Added int converter
    path('edit_edu/<int:edu_id>/',views.edit_edu,name='edit_edu'), # Added int converter
    path('<int:user_id>/edit_edu/<int:edu_id>/',views.edit_edu,name='edit_edu_admin'), # Added int converter
    path('delate_cert/<int:cert_id>/',views.delate_cert,name='delate_cert'), # Added int converter
    path('<int:user_id>/delate_cert/<int:cert_id>/',views.delate_cert,name='delate_cert_admin'), # Added int converter
    path('edit_cert/<int:cert_id>/',views.edit_cert,name='edit_cert'), # Added int converter
    path('<int:user_id>/edit_cert/<int:cert_id>/',views.edit_cert,name='edit_cert_admin'), # Added int converter
    path('add_cert/',views.add_cert,name='add_cert'),
    path('<int:user_id>/add_cert/',views.add_cert,name='add_cert_admin'), # Added int converter
    path('add_exp/',views.add_exp,name='add_exp'),
    path('<int:user_id>/add_exp/',views.add_exp,name='add_exp_admin'), # Added int converter
    path('add_skill/',views.add_skill,name='add_skill'),
    path('<int:user_id>/add_skill/',views.add_skill,name='add_skill_admin'), # Added int converter
    path('add_edu/',views.add_edu,name='add_edu'),
    path('<int:user_id>/add_edu/',views.add_edu,name='add_edu_admin'), # Changed <user_id> to <int:user_id>
    path('add_language/',views.add_language,name='add_language'),
    path('<int:user_id>/add_language/',views.add_language,name='add_language_admin'), # Added int converter
    path('export/pdf/', views.export_cv_pdf, name='export_cv_pdf'),
    path('export/pdf/<int:user_id>/', views.export_cv_pdf, name='export_cv_pdf_admin'), # Changed <user_id> to <int:user_id>
    path('profile/view/export/pdf/<int:user_id>/', views.student_company_export_cv_pdf, name='student_company_export_cv_pdf'),
    path('student/<int:student_id>/view/', views.company_student_profile, name='company_student_profile'),
    path('company/<int:company_id>/', views.public_company_profile_view, name='public_company_profile'),
      path('company/edit-requests/',views.company_edit_requests,name='company_edit_requests'),
]


