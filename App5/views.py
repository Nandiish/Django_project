from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Data,Signup


# Create your views here.
def main(request):
    destinations = Data.objects.all()
    return render(request, 'main.html', {'destination': destinations})

def signup(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        PASSWORD = request.POST.get('PASSWORD')
        rpass = request.POST.get('rpass')
        email = request.POST.get('epass')

        if PASSWORD != rpass:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # Save the new user in the database
        if Signup.objects.filter(user=user).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        obj = Signup()
        obj.user = user
        obj.pasw = make_password(PASSWORD)  # Hash password before saving
        obj.email = email
        obj.save()

        messages.success(request, "Sign-up successful!")
        return redirect('login')  # Redirect to login page after successful sign-up
    return render(request, 'signup.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        try:
            user_obj = Signup.objects.get(user=username)
            if check_password(password, user_obj.pasw):  # Check hashed password
                # Set session data for logged-in user
                request.session['username'] = username
                messages.success(request, "Login successful!")
                return redirect('dashboard')  # Redirect to the dashboard after login
            else:
                messages.error(request, "Invalid password. Please try again.")
        except Signup.DoesNotExist:
            messages.error(request, "User does not exist. Please sign up first.")
    return render(request, 'login.html')


def dashboard(request):
    username=request.session.get('username')
    return render(request, 'dashboard.html',{'username':username})  # You can replace this with your actual dashboard page
