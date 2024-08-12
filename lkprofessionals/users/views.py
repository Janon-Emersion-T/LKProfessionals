from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from core.models import *
from core.forms import *

#signupview
def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the profile page
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


#login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the profile page
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

#logout
def logout_view(request):
    logout(request)
    return redirect('login')

#dashboard
@login_required
def dashboard_view(request):
    return render(request, 'users/dashboard.html')

@login_required
def view_profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'users/dashboard/view_profile.html', {'profile': profile})

@login_required
def view_contactdetail(request):
    contactdetail = ContactDetail.objects.get(user=request.user)
    return render(request, 'users/dashboard/view_contactdetail.html', {'contactdetail': contactdetail})

@login_required
def view_socialmedia(request):
    socialmedia = SocialMedia.objects.get(user=request.user)
    return render(request, 'users/dashboard/view_socialmedia.html', {'socialmedia': socialmedia})

@login_required
def view_education(request):
    education = Education.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_education.html', {'education': education})

@login_required
def view_experience(request):
    experience = Experience.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_experience.html', {'experience': experience})

@login_required
def view_careerbreak(request):
    careerbreak = CareerBreak.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_careerbreak.html', {'careerbreak': careerbreak})

@login_required
def view_service(request):
    service = Service.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_service.html', {'service': service})

@login_required
def view_language(request):
    language = Language.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_language.html', {'language': language})

@login_required
def view_volunteerexperience(request):
    volunteerexperience = VolunteerExperience.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_volunteerexperience.html', {'volunteerexperience': volunteerexperience})

@login_required
def view_project(request):
    project = Project.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_project.html', {'project': project})

@login_required
def view_certification(request):
    certification = Certification.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_certification.html', {'certification': certification})

@login_required
def view_recommendation(request):
    recommendation = Recommendation.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_recommendation.html', {'recommendation': recommendation})

@login_required
def view_publication(request):
    publication = Publication.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_publication.html', {'publication': publication})

@login_required
def view_patent(request):
    patent = Patent.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_patent.html', {'patent': patent})

@login_required
def view_honoraward(request):
    honoraward = HonorAward.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_honoraward.html', {'honoraward': honoraward})

@login_required
def view_testscore(request):
    testscore = TestScore.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_testscore.html', {'testscore': testscore})

@login_required
def view_organization(request):
    organization = Organization.objects.filter(user=request.user)
    return render(request, 'users/dashboard/view_organization.html', {'organization': organization})

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/dashboard/edit_profile.html', {'form': form})

@login_required
def edit_contactdetail(request):
    contactdetail = ContactDetail.objects.get(user=request.user)
    if request.method == 'POST':
        form = ContactDetailForm(request.POST, instance=contactdetail)
        if form.is_valid():
            form.save()
            return redirect('view_contactdetail')
    else:
        form = ContactDetailForm(instance=contactdetail)
    return render(request, 'users/dashboard/edit_contactdetail.html', {'form': form})

@login_required
def edit_socialmedia(request):
    socialmedia = SocialMedia.objects.get(user=request.user)
    if request.method == 'POST':
        form = SocialMediaForm(request.POST, instance=socialmedia)
        if form.is_valid():
            form.save()
            return redirect('view_socialmedia')
    else:
        form = SocialMediaForm(instance=socialmedia)
    return render(request, 'users/dashboard/edit_socialmedia.html', {'form': form})

@login_required
def edit_education(request):
    education = Education.objects.get(user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('view_education')
    else:
        form = EducationForm(instance=education)
    return render(request, 'users/dashboard/edit_education.html', {'form': form})

@login_required
def edit_experience(request):
    experience = Experience.objects.get(user=request.user)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            return redirect('view_experience')
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'users/dashboard/edit_experience.html', {'form': form})

@login_required
def edit_careerbreak(request):
    careerbreak = CareerBreak.objects.get(user=request.user)
    if request.method == 'POST':
        form = CareerBreakForm(request.POST, instance=careerbreak)
        if form.is_valid():
            form.save()
            return redirect('view_careerbreak')
    else:
        form = CareerBreakForm(instance=careerbreak)
    return render(request, 'users/dashboard/edit_careerbreak.html', {'form': form})

@login_required
def edit_service(request):
    service = Service.objects.get(user=request.user)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('view_service')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'users/dashboard/edit_service.html', {'form': form})

@login_required
def edit_language(request):
    language = Language.objects.get(user=request.user)
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('view_language')
    else:
        form = LanguageForm(instance=language)
    return render(request, 'users/dashboard/edit_language.html', {'form': form})

@login_required
def edit_volunteerexperience(request):
    volunteerexperience = VolunteerExperience.objects.get(user=request.user)
    if request.method == 'POST':
        form = VolunteerExperienceForm(request.POST, instance=volunteerexperience)
        if form.is_valid():
            form.save()
            return redirect('view_volunteerexperience')
    else:
        form = VolunteerExperienceForm(instance=volunteerexperience)
    return render(request, 'users/dashboard/edit_volunteerexperience.html', {'form': form})

@login_required
def edit_project(request):
    project = Project.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('view_project')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'users/dashboard/edit_project.html', {'form': form})

@login_required
def edit_certification(request):
    certification = Certification.objects.get(user=request.user)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('view_certification')
    else:
        form = CertificationForm(instance=certification)
    return render(request, 'users/dashboard/edit_certification.html', {'form': form})

@login_required
def edit_recommendation(request):
    recommendation = Recommendation.objects.get(user=request.user)
    if request.method == 'POST':
        form = RecommendationForm(request.POST, instance=recommendation)
        if form.is_valid():
            form.save()
            return redirect('view_recommendation')
    else:
        form = RecommendationForm(instance=recommendation)
    return render(request, 'users/dashboard/edit_recommendation.html', {'form': form})

@login_required
def edit_publication(request):
    publication = Publication.objects.get(user=request.user)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('view_publication')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'users/dashboard/edit_publication.html', {'form': form})

@login_required
def edit_patent(request):
    patent = Patent.objects.get(user=request.user)
    if request.method == 'POST':
        form = PatentForm(request.POST, instance=patent)
        if form.is_valid():
            form.save()
            return redirect('view_patent')
    else:
        form = PatentForm(instance=patent)
    return render(request, 'users/dashboard/edit_patent.html', {'form': form})

@login_required
def edit_honoraward(request):
    honoraward = HonorAward.objects.get(user=request.user)
    if request.method == 'POST':
        form = HonorAwardForm(request.POST, instance=honoraward)
        if form.is_valid():
            form.save()
            return redirect('view_honoraward')
    else:
        form = HonorAwardForm(instance=honoraward)
    return render(request, 'users/dashboard/edit_honoraward.html', {'form': form})

@login_required
def edit_testscore(request):
    testscore = TestScore.objects.get(user=request.user)
    if request.method == 'POST':
        form = TestScoreForm(request.POST, instance=testscore)
        if form.is_valid():
            form.save()
            return redirect('view_testscore')
    else:
        form = TestScoreForm(instance=testscore)
    return render(request, 'users/dashboard/edit_testscore.html', {'form': form})

@login_required
def edit_organization(request):
    organization = Organization.objects.get(user=request.user)
    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('view_organization')
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'users/dashboard/edit_organization.html', {'form': form})

