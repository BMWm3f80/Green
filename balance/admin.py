from django.contrib import admin
from .models import *


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    inlines = [ModuleInline, ]
    pass


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass


class PermissionInline(admin.TabularInline):
    model = Permission
    extra = 0


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    inlines = [PermissionInline, ]
    pass


@admin.register(RoleUser)
class RoleUserAdmin(admin.ModelAdmin):
    pass







