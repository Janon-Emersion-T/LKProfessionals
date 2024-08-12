from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('contact-details/', views.contact_detail_view, name='contact_detail_view'),
    path('social-media/', views.social_media_view, name='social_media_view'),
    path('education/', views.education_view, name='education_view'),
    path('experience/', views.experience_view, name='experience_view'),
    path('career-break/', views.career_break_view, name='career_break_view'),
    path('service/', views.service_view, name='service_view'),
    path('language/', views.language_view, name='language_view'),
    path('volunteer-experience/', views.volunteer_experience_view, name='volunteer_experience_view'),
    path('project/', views.project_view, name='project_view'),
    path('certification/', views.certification_view, name='certification_view'),
    path('recommendation/', views.recommendation_view, name='recommendation_view'),
    path('publication/', views.publication_view, name='publication_view'),
    path('patent/', views.patent_view, name='patent_view'),
    path('honor-award/', views.honor_award_view, name='honor_award_view'),
    path('test-score/', views.test_score_view, name='test_score_view'),
    path('organization/', views.organization_view, name='organization_view'),
]
