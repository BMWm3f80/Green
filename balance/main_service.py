from .models import *


def get_user_apps(user):
    app_list = []
    apps = App.objects.filter(appuser__user=user)
    for app in apps:
        a = {'code': app.code,
             'name': app.name,
             'description': app.description,
             'icon': app.icon}
        app_list.append(a)
    return app_list


def get_app_modules(app_code, user):
    app_modules = Module_User.objects.filter(module__app__code=app_code, user=user, module__active=True)
    return app_modules


def get_app(app_code):
    return App.objects.get(code=app_code)
