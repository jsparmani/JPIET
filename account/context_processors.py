from .import models

def UserList(request):
    admin_all = [u['user'] for u in models.AdminUser.objects.all().values('user')]
    frontend_all = [u['user'] for u in models.FrontEndUser.objects.all().values('user')]
    

    return {'admin_all':admin_all, 'frontend_all':frontend_all}