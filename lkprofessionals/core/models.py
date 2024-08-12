from django.db import models
from django.contrib.auth.models import User
from datetime import date

def get_default_date():
    return date.today()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/profiles/', blank=True, null=True)
    headline = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    dob = models.DateField(default=date(1991, 10, 12))
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class ContactDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    whatsapp_link = models.URLField(blank=True)

    def __str__(self):
        return f"Contact for {self.user.username}"

class SocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    whatsapp_link = models.URLField(blank=True)


    def __str__(self):
        return f"Social Media for {self.user.username}"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255, blank=True)
    field_of_study = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.degree} at {self.school}"

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_current = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title} at {self.company}"

class CareerBreak(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"Career Break for {self.user.username}"

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Language(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Fluent', 'Fluent'),
        ('Native', 'Native')
    ], default='Intermediate')

    def __str__(self):
        return self.language

class VolunteerExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} at {self.organization}"

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=255, blank=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_recommendations')
    recommender_name = models.CharField(max_length=255)
    recommender_contact = models.CharField(max_length=255)
    recommender_position = models.CharField(max_length=255, blank=True)
    relationship = models.CharField(max_length=255, blank=True)
    recommendation_text = models.TextField()

    def __str__(self):
        return f"Recommendation by {self.recommender_name}"

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Patent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    patent_number = models.CharField(max_length=255)
    filing_date = models.DateField()
    issue_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.patent_number}"

class HonorAward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    issuing_organization = models.CharField(max_length=255)
    issue_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class TestScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=255)
    score = models.CharField(max_length=50)
    date_taken = models.DateField()
    description = models.TextField(blank=True)
    text_url = models.URLField(blank=True)


    def __str__(self):
        return f"{self.test_name} - {self.score}"

class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    organization_url = models.URLField(blank=True)


    def __str__(self):
        return self.name
