from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from core.models import OKR

from .forms import OKRModelForm


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'okrs'

    def get_queryset(self):
        return OKR.objects.all()


def register(request):
    form = OKRModelForm()
    status = 201

    if request.method == 'POST':
        form = OKRModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'OKR registered successfully!')
            form = OKRModelForm()
        else:
            messages.error(request, 'Error registering OKR!')
            status = 200

    return render(request, 'core/register.html', {'form': form}, status=status)
