from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import balance.main_service as service_main


@login_required
def modules_view(request):
    app_code = request.GET.get('app_code')
    app = service_main.get_app(app_code)
    app_modules = service_main.get_app_modules(app_code, request.user)
    return render(request, 'modules.html', {"app_modules": app_modules,
                                            "app": app})
