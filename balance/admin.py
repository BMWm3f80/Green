from django.contrib import admin
from .models import *


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class PermissionInline(admin.TabularInline):
    model = Permission
    extra = 0


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    inlines = [ModuleInline, ]
    pass


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ PermissionInline, ]










