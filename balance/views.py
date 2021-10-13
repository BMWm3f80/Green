from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def modules_view(request):
    print(request.GET.get('app_code'))
