from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
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
            return HttpResponseRedirect('link', {'original_link': original_link,
                                                 'lil_slug': lil_slug})

    form = LinkGeneratorForm()
    return render(request, 'LinkGenerator/index.html', {'form': form})


def response_view(request):
    return render(request, 'LinkGenerator/response.html')
