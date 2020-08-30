from django.shortcuts import render

# Simple functional view for testing purposes
def base_page_view(request):
    return render(request, 'pages/base.html')