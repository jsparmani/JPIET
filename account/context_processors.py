from .import models

def UserList(request):
    admin_list = [u['user'] for u in models.AdminUser.objects.all().values('user')]
    frontend_list = [u['user'] for u in models.FrontEndUser.objects.all().values('user')]
    

    return {'admin_list':admin_list, 'frontend_list':frontend_list}