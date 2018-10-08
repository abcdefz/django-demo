from django.db import models


class MenuPermission(models.Model):
    name = models.CharField(max_length=64)


class ApiPermission(models.Model):
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=32)
    name = models.CharField(max_length=32)


class ResourcePermission(models.Model):
    path = models.CharField(max_length=32)
    name = models.CharField(max_length=32)


class Role(models.Model):
    name = models.CharField(max_length=32)
    api_permission = models.ManyToManyField(
        ApiPermission, blank=True, related_name='role')
    resource_permission = models.ManyToManyField(
        ResourcePermission, blank=True, related_name='role')

    def __str__(self):
        return f'<Role-{self.id} {self.name}>'


class User(models.Model):
    name = models.CharField(max_length=32, null=True)
    role = models.ManyToManyField(Role, blank=True, related_name='user')

    def verify_auth_token(token):
        return False
    
    def verify_api_perimission(**permission):
        if not user.role.filter(
                permission__method=permission['method'],
                permission__path=permission['path'],
                permission__name=permission['name']):
            return False
        return True
    
    def verify_resource_permission(**permission):
        if not user.role.filter(
                resource_permission__path=permission['path'],
                resource_permission__name=permission['name'])
            return False
        return True

    def __str__(self):
        return f'<User-{self.id} {self.name}>'
