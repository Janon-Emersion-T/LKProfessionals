from django import forms
from .models import Profile, ContactDetail, SocialMedia, Education, Experience, CareerBreak, Service, Language, VolunteerExperience, Project, Certification, Recommendation, Publication, Patent, HonorAward, TestScore, Organization

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'middle_name', 'last_name','profile_picture', 'headline', 'bio', 'dob', 'is_active']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = ['email', 'telephone', 'address', 'whatsapp_link']

class SocialMediaForm(forms.ModelForm):
    class Meta:
        model = SocialMedia
        fields = ['facebook', 'instagram', 'linkedin', 'twitter', 'youtube', 'whatsapp_link']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'field_of_study', 'start_date', 'end_date', 'description', 'is_current']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'company', 'start_date', 'end_date', 'description', 'is_current']

class CareerBreakForm(forms.ModelForm):
    class Meta:
        model = CareerBreak
        fields = ['start_date', 'end_date', 'reason']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language', 'proficiency']

class VolunteerExperienceForm(forms.ModelForm):
    class Meta:
        model = VolunteerExperience
        fields = ['organization', 'role', 'start_date', 'end_date', 'description']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'link']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuing_organization', 'issue_date', 'expiration_date', 'credential_id', 'credential_url']

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ['recommender_name', 'recommender_contact', 'recommender_position', 'relationship', 'recommendation_text']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'publication_date', 'publisher', 'url', 'description']

class PatentForm(forms.ModelForm):
    class Meta:
        model = Patent
        fields = ['title', 'patent_number', 'filing_date', 'issue_date', 'description']

class HonorAwardForm(forms.ModelForm):
    class Meta:
        model = HonorAward
        fields = ['title', 'issuing_organization', 'issue_date', 'description']

class TestScoreForm(forms.ModelForm):
    class Meta:
        model = TestScore
        fields = ['test_name', 'score', 'date_taken', 'text_url', 'description']

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'position', 'start_date', 'end_date', 'description', 'organization_url']
