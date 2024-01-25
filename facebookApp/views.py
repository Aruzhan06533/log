from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import User  # Import your User model

def loadPage(request):
    return render(request, 'loading.html')
def indexPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Save data to the database
            user = User(email=email, password=password)
            user.save()

            return redirect('loadPage')
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return render(request, 'index.html')