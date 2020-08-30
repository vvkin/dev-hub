from django.shortcuts import render

# Simple functional view for testing purposes
def home_page_view(request):
    return render(request, 'pages/home.html')