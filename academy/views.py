from django.shortcuts import render

def home(request):

    context = {
        'page_title': 'Academy',
        'nav_name': 'core_home'
    }

    return render(request, 'academy/index.html', context)
