from django.shortcuts import render

# Create your views here.
# Functions below handle requests passed along by _djproject/urls.py
def home_view(request):
    return render(request,'allpages/index.html',{'title': 'Your Site Title'})

def about_view(request):
    return render(request,'allpages/about.html',{'title': 'About Us'})

def privacy_view(request):
    return render(request,'allpages/privacy.html',{'title': 'Privacy Policy'})