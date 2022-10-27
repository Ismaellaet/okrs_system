from django.shortcuts import render
from django.contrib import messages

from .forms import OKRModelForm


def register(request):
    form = OKRModelForm()

    if request.method == 'POST':
        form = OKRModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'OKR registered successfully!')
            form = OKRModelForm()
        else:
            messages.error(request, 'Error registering OKR!')

    return render(request, 'core/index.html', {'form': form})
