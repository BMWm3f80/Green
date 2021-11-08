from django.db import models
from django.contrib.auth.models import User


class App(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    icon = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name


class AppUser(models.Model):
    app = models.ForeignKey(App, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}-{}".format(self.app.code, self.user.username)


class Module(models.Model):
    app = models.ForeignKey(App, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=128, null=True)
    path = models.CharField(max_length=256, null=True, blank=True)
    icon = models.CharField(max_length=128, null=True, blank=True)
    box_class = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    module = models.ForeignKey(Module, null=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class RoleUser(models.Model):
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}-{}".format(self.role.code, self.user.username)


class Permission(models.Model):
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=True)


class UserPermission(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    permission = models.ForeignKey(Permission, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}-{}".format(self.user.username, self.permission.code)


###################


class Company(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField()
    status = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=1000)

    def __str__(self):
        return self.name


class Stuff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "{}-{}".format(self.user.username, self.user.last_name)
