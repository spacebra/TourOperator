from operators.forms import *
#def login(request):
#    from django.contrib.auth.views import login
#    return login(request, authentication_form=LoginForm)
    
    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(username=username, password=password)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import RequestContext

def operator_login(request):    
    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                pass
        else:
            # Return an 'invalid login' error message.
            pass
    else:
        form = LoginForm()

    context = RequestContext(request, {
        'action': '',
        'form': form,
    })
    return render_to_response('registration/login.html', context)

def operator_logout(request):
    logout(request)
    form = LoginForm()

    context = RequestContext(request, {
        'action': '',
        'form': form,
    })

    return redirect('/login')