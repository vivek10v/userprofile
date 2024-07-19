from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Profile, Project, Education, Certification, WorkExperience
from .forms import ProfileForm, ProjectForm, EducationForm, CertificationForm, WorkExperienceForm
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages


def Reg_user(request):
    
    if request.method=='POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'This username already exists')
                return redirect(request, 'registration/login.html')
            # elif User.objects.filter(email= email).exists():
            #     messages.info(request, 'This mail id already exists')
            #     return redirect(request, 'registration/login.html')
            
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
            return redirect('profile')
        
        else:
            messages.info(request, 'This password not matching')
            return redirect(request, 'registration/login.html')
        
    return redirect(request, 'registration/login.html')
    
 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request, user)
            auth_login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    projects = Project.objects.filter(user=request.user)
    educations = Education.objects.filter(user=request.user)
    certifications = Certification.objects.filter(user=request.user)
    work_experiences = WorkExperience.objects.filter(user=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.instance.user = request.user
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=profile)

    context = {
        'profile_form': profile_form,
        'projects': projects,
        'educations': educations,
        'certifications': certifications,
        'work_experiences': work_experiences,
    }
    return render(request, 'profiles/profile.html', context)


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('profile')
    else:
        form = ProjectForm()

    return render(request, 'profiles/add_project.html', {'form': form})


def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'profiles/edit_project.html', {'form': form})


def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('profile')
    return render(request, 'profiles/delete_project.html', {'project': project})


def add_education(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('profile')
    else:
        form = EducationForm()

    return render(request, 'profiles/add_education.html', {'form': form})


def edit_education(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EducationForm(instance=education)
    return render(request, 'profiles/edit_education.html', {'form': form})


def delete_education(request, pk):
    education = get_object_or_404(Education, pk=pk, user=request.user)
    if request.method == 'POST':
        education.delete()
        return redirect('profile')
    return render(request, 'profiles/delete_education.html', {'education': education})


def add_certification(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            certification = form.save(commit=False)
            certification.user = request.user
            certification.save()
            return redirect('profile')
    else:
        form = CertificationForm()

    return render(request, 'profiles/add_certification.html', {'form': form})


def edit_certification(request, pk):
    certification = get_object_or_404(Certification, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CertificationForm(request.POST, instance=certification)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CertificationForm(instance=certification)
    return render(request, 'profiles/edit_certification.html', {'form': form})


def delete_certification(request, pk):
    certification = get_object_or_404(Certification, pk=pk, user=request.user)
    if request.method == 'POST':
        certification.delete()
        return redirect('profile')
    return render(request, 'profiles/delete_certification.html', {'certification': certification})


def add_work_experience(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            work_experience = form.save(commit=False)
            work_experience.user = request.user
            work_experience.save()
            return redirect('profile')
    else:
        form = WorkExperienceForm()

    return render(request, 'profiles/add_work_experience.html', {'form': form})


def edit_work_experience(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = WorkExperienceForm(instance=work_experience)
    return render(request, 'profiles/edit_work_experience.html', {'form': form})


def delete_work_experience(request, pk):
    work_experience = get_object_or_404(WorkExperience, pk=pk, user=request.user)
    if request.method == 'POST':
        work_experience.delete()
        return redirect('profile')
    return render(request, 'profiles/delete_work_experience.html', {'work_experience': work_experience})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')
    
# def logOut(request):
#     authenticate.logout(request)
#     return redirect(request, 'registration/login.html')
    
def home(request):
    return render(request, 'profiles/home.html')

def index(request):
    return render(request, 'index.html')