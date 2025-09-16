from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import DonorForm
from .models import Donor

@login_required
def home(request):
    return render(request, 'donors/index.html')


def donor_register(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Donor registered successfully!')
            return redirect('donor_register')
        else:
            messages.error(request, '❌ Please correct the errors below.')
    else:
        form = DonorForm()
    return render(request, 'donors/donor_form.html', {'form': form})


@login_required
def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donors/donor_list.html', {'donors': donors})


def search_donors(request):
    donors = []
    if request.method == "POST":
        blood_group = request.POST.get("blood_group")
        city = request.POST.get("city")

        donors = Donor.objects.all()
        if blood_group:
            donors = donors.filter(blood_group=blood_group)
        if city:
            donors = donors.filter(city__icontains=city)

    return render(request, "donors/search.html", {"donors": donors})


# ---------------------
# User Authentication Views
# ---------------------




def login_view(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Change to your homepage
        else:
            context['error'] = 'Invalid username or password.'

    return render(request, 'donors/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login') 


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        hospital_name = request.POST.get('hospital_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        email = request.POST.get('email')
        hospital_address = request.POST.get('hospital_address')
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, "❌ Email already registered.")
            return redirect('register')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        # Optional: Save hospital-related info in another model if needed

        messages.success(request, "✅ Registered successfully! Please log in.")
        return redirect('login')

    return render(request, 'donors/register.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')  # Using email as username for login
        password = request.POST.get('password')

        # Validate required fields
        if not username or not password:
            return render(request, 'donors/register.html', {'error': 'Email and password are required.'})

        # Check if user exists
        if User.objects.filter(username=username).exists():
            return render(request, 'donors/register.html', {'error': 'Email already registered.'})

        # Create user
        user = User.objects.create_user(username=username, email=username, password=password)

        # Save additional hospital data here if you have a model for that

        login(request, user)
        return redirect('index')

    return render(request, 'donors/register.html')


def view_all_donors(request):
    donors = Donor.objects.all()
    return render(request, 'donors/view_all_donors.html', {'donors': donors})

