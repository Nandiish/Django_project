from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.db import IntegrityError
from .models import Signup,Data


# Sign-up view
def main(request):
    destinations = Data.objects.all()
    return render(request, 'main.html', {'destination': destinations})

# def signup(request):
#     if request.method == 'POST':
#         user = request.POST.get('user')
#         PASSWORD = request.POST.get('PASSWORD')
#         rpass = request.POST.get('rpass')
#         email = request.POST.get('epass')

#         if PASSWORD != rpass:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')

      
#         if Signup.objects.filter(user=user).exists():
#             messages.error(request, "Username already taken.")
#             return redirect('signup')

#         obj = Signup()
#         obj.user = user
#         obj.pasw = make_password(PASSWORD)  
#         obj.email = email
#         obj.save()

#         messages.success(request, "Sign-up successful!")
#         return redirect('login')  
#     return render(request, 'signup.html')



def signup(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pasw = request.POST.get('pasw')
        rpass = request.POST.get('rpass')
        email = request.POST.get('email')

        # Ensure password and repeat password match
        if pasw != rpass:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Check if the email is already taken
        if Signup.objects.filter(email=email).exists():
            messages.error(request, "This email is already registered. Please use a different email.")
            return redirect('signup')

        try:
            # Save the user if email is unique
            obj = Signup(user=user, pasw=make_password(pasw), email=email)
            obj.save()
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "An error occurred while processing your request. Please try again.")
    return render(request, 'signup.html')


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        try:
            user_obj = Signup.objects.get(user=username)
            if check_password(password, user_obj.pasw): 
                request.session['username'] = username 
                messages.success(request, "Login successful!")
                return redirect('dashboard')  # Redirect to the dashboard after login
            else:
                messages.error(request, "Invalid password. Please try again.")
        except Signup.DoesNotExist:
            messages.error(request, "User does not exist. Please sign up first.")
    return render(request, 'login.html')

# Dashboard view (after login)
def dashboard(request):
    username=request.session.get('username')
    return render(request, 'dashboard.html',{'username':username})  # You can replace this with your actual dashboard page

def data_changelist(request):
    return render(request, 'data_changelist.html')