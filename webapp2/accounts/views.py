from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Fired every time a request hits the 'signup/' URL
# Need to differentiate between POST and GET requests
def signup_view(request):
    if request.method == 'POST':
        # Sending data into the form for validation
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # REMINDER: log user in here
            
            # Redirect user to articles URL named list (article homepage)
            return redirect('articles:list')
    
    else:
        form = UserCreationForm()
    
    # Send instance of form to the template
    return render(request, 'accounts/signup.html', { 'form': form })


def login_view(request):
    if request.method == 'POST':
        # Validation
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # REMINDER: Log the user in.
            return redirect('articles:list')
    
    # If GET    
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', { 'form': form })

