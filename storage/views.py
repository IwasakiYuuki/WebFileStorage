from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def top(request):
    return render(request, 'storage/top.html', {})
