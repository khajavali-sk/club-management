from django.shortcuts import redirect,HttpResponseRedirect


def index(request):
    return redirect('authentication/')