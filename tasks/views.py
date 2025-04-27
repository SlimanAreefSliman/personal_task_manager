from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to the Task Manager! <a href='/admin/'>Go to Admin</a> or <a href='/login/'>Login</a>")
