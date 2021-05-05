from django.shortcuts import render
# from django.http import HttpResponse

def homepage(request):
    return render(request, 'homepage.html')
    #return HttpResponse('homepage')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('about')