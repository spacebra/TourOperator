from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import RequestContext

from program.models import Program, Picture
from program.forms import *


def create(request):
    if not request.user.is_authenticated():
        return redirect('/login')

    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            price = form.cleaned_data.get('price')
            program = Program(title=title, description=description, price=price)
            program.save()

            url = "xxxxxa"
            #url = form.data.get('picture')
            #picture = Picture(url=url, related_program=program)
            #picture.save()

            return render_to_response('view_program.html', {'program': program, 'url':url})

    else:
        form = CreateForm()

    #context = {
    #    'action': '',
    #    'form': form,
    #}
    #context.update(csrf(request))

    #return render_to_response('create.html', context)
    
    context = RequestContext(request, {
        'action': '',
        'form': form,
    })

    return render_to_response('create.html', context)

def edit_program(request, program_id):
    program = Program.objects.get(id=program_id)
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)

        if form.is_valid():
            program.title = form.cleaned_data.get('title')
            program.description = form.cleaned_data.get('description')
            program.price = form.cleaned_data.get('price')

            program.save()

            url = "xxxxx"
            #url = form.data.get('picture')
            #picture = Picture(url=url, related_program=program)
            #picture.save()

            return render_to_response('view_program.html', {'program': program, 'url':url})

    else:
        defaults = {
            'title': program.title,
            'description': program.description,
            'price': program.price,

        }
        form = CreateForm(defaults)
        
    context = RequestContext(request, {
        'action': '',
        'form': form,
    })

    return render_to_response('edit_program.html', context)

def delete_program(request, program_id):
    program = Program.objects.get(id=program_id)
    program.delete()

    program_all = Program.objects.all()
    return redirect('/', {'programs': program_all})



def view_all(request):
    programs = Program.objects.all()

    context = RequestContext(request, {
        'programs': programs,
    })

    return render_to_response('view_all.html', context)

def view_program(request, program_id):
    program = Program.objects.get(id=program_id)
    url = 'image is temporary disabled ^^" '
    context = RequestContext(request, {
        'program': program,
        'url': url,
    })

    return render_to_response('view_program.html', context)