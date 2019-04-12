from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from .forms import LinkGeneratorForm


# Create your views here.
def index_view(request):
    if request.method == 'POST':
        form = LinkGeneratorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('link')

    form = LinkGeneratorForm()
    return render(request, 'LinkGenerator/index.html', {'form': form})


def response_view(request):
    return HttpResponse('Works')
