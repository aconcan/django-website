from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    # Sending instance of the form to the template
    return render(request, 'accounts/signup.html', { 'form': form })

