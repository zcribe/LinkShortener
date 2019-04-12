from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .forms import LinkGeneratorForm
from .models import RedirectorModel
from .helper import random_slugger


# Create your views here.
def index_view(request):
    if request.method == 'POST':
        form = LinkGeneratorForm(request.POST)
        if form.is_valid():
            original_link = form.cleaned_data.get('original_link')
            lil_slug = random_slugger()
            new = RedirectorModel(original_link=original_link, id_slug=lil_slug)
            new.save()
            request.session['original_link'] = original_link
            request.session['lil_slug'] = lil_slug
            return HttpResponseRedirect('link')

    form = LinkGeneratorForm()
    return render(request, 'LinkGenerator/index.html', {'form': form})


def response_view(request):
    originl_link = request.session.get('original_link')
    lil_slug = request.session.get('lil_slug')
    return render(request, 'LinkGenerator/response.html', {'original_link': originl_link,
                                                           'lil_slug': lil_slug})


def redirect_view(request, slug):
    redir = RedirectorModel.objects.filter(id_slug=slug).get()
    return HttpResponseRedirect(redir.original_link)
