from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from .forms import SnippetForm
from .models import Snippet

class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/home.html'

    def get_context_data(self, **kwargs):
        context = super(SnippetListView, self).get_context_data(**kwargs)
        return context

class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/detail.html'

def add(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            # Create and save directly.
            Snippet(
             title=form.cleaned_data['title'], 
             language=form.cleaned_data['language'],
             snippet=form.cleaned_data['snippet'],
             description=form.cleaned_data['description']).save()
            return redirect('snippets:home')
        else:
            # Render form with errors.
            return render(request, 'snippets/add.html', { 'form' : form })
    else:
        # If the user sends a GET request...
        context = { 'header' : 'GET', 'form' : SnippetForm() }
        return render(request, 'snippets/add.html', context)
