from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import *

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})

@login_required
def contact_detail_view(request):
    if request.method == 'POST':
        form = ContactDetailForm(request.POST, instance=request.user.contactdetail)
        if form.is_valid():
            form.save()
            return redirect('contact_detail_view')
    else:
        form = ContactDetailForm(instance=request.user.contactdetail)
    return render(request, 'core/contact_detail_form.html', {'form': form})

@login_required
def social_media_view(request):
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, instance=request.user.socialmedia)
        if form.is_valid():
            form.save()
            return redirect('social_media_view')
    else:
        form = SocialMediaForm(instance=request.user.socialmedia)
    return render(request, 'core/social_media_form.html', {'form': form})

@login_required
def education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('education_view')
    else:
        form = EducationForm()
    return render(request, 'core/education_form.html', {'form': form})

@login_required
def experience_view(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = request.user
            experience.save()
            return redirect('experience_view')
    else:
        form = ExperienceForm()
    return render(request, 'core/experience_form.html', {'form': form})

@login_required
def career_break_view(request):
    if request.method == 'POST':
        form = CareerBreakForm(request.POST)
        if form.is_valid():
            career_break = form.save(commit=False)
            career_break.user = request.user
            career_break.save()
            return redirect('career_break_view')
    else:
        form = CareerBreakForm()
    return render(request, 'core/career_break_form.html', {'form': form})

@login_required
def service_view(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect('service_view')
    else:
        form = ServiceForm()
    return render(request, 'core/service_form.html', {'form': form})

@login_required
def language_view(request):
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            language = form.save(commit=False)
            language.user = request.user
            language.save()
            return redirect('language_view')
    else:
        form = LanguageForm()
    return render(request, 'core/language_form.html', {'form': form})

@login_required
def volunteer_experience_view(request):
    if request.method == 'POST':
        form = VolunteerExperienceForm(request.POST)
        if form.is_valid():
            volunteer_experience = form.save(commit=False)
            volunteer_experience.user = request.user
            volunteer_experience.save()
            return redirect('volunteer_experience_view')
    else:
        form = VolunteerExperienceForm()
    return render(request, 'core/volunteer_experience_form.html', {'form': form})

@login_required
def project_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_view')
    else:
        form = ProjectForm()
    return render(request, 'core/project_form.html', {'form': form})

@login_required
def certification_view(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user = request.user
            certification.save()
            return redirect('certification_view')
    else:
        form = CertificationForm()
    return render(request, 'core/certification_form.html', {'form': form})

@login_required
def recommendation_view(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.save()
            return redirect('recommendation_view')
    else:
        form = RecommendationForm()
    return render(request, 'core/recommendation_form.html', {'form': form})

@login_required
def publication_view(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.user = request.user
            publication.save()
            return redirect('publication_view')
    else:
        form = PublicationForm()
    return render(request, 'core/publication_form.html', {'form': form})

@login_required
def patent_view(request):
    if request.method == 'POST':
        form = PatentForm(request.POST)
        if form.is_valid():
            patent = form.save(commit=False)
            patent.user = request.user
            patent.save()
            return redirect('patent_view')
    else:
        form = PatentForm()
    return render(request, 'core/patent_form.html', {'form': form})

@login_required
def honor_award_view(request):
    if request.method == 'POST':
        form = HonorAwardForm(request.POST)
        if form.is_valid():
            honor_award = form.save(commit=False)
            honor_award.user = request.user
            honor_award.save()
            return redirect('honor_award_view')
    else:
        form = HonorAwardForm()
    return render(request, 'core/honor_award_form.html', {'form': form})

@login_required
def test_score_view(request):
    if request.method == 'POST':
        form = TestScoreForm(request.POST)
        if form.is_valid():
            test_score = form.save(commit=False)
            test_score.user = request.user
            test_score.save()
            return redirect('test_score_view')
    else:
        form = TestScoreForm()
    return render(request, 'core/test_score_form.html', {'form': form})

@login_required
def organization_view(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.user = request.user
            organization.save()
            return redirect('organization_view')
    else:
        form = OrganizationForm()
    return render(request, 'core/organization_form.html', {'form': form})
