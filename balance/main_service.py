from .models import *


def get_user_privilages(user):
    app_list = []
    module_list = []
    apps = App.objects.filter(appuser__user=user)
    for app in apps:
        a = {}
        a['code'] = app.code
        a['name'] = app.name
        a['description'] = app.description
        a['icon'] = app.icon
        modules = Module.objects.filter(app=app, active=True)
        # for module in modules:
        #     m = {}
        #     m['id'] = module.id
        #     m['name'] = module.name
        #     m['path'] = module.path
        #     m['icon'] = module.icon
        #     m['app'] = module.app.name
        #     module_list.append(m)
        # a['modules'] = module_list
        app_list.append(a)
        # module_list = []
    return app_list


def get_app_modules(app_code, user):
    modules = Module.objects.filter(app__code=app_code, app__appuser=user)
    return modules

