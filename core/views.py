from django.shortcuts import render
from django.contrib import messages

from .forms import OKRModelForm


def register(request):
    form = OKRModelForm()
    status = 201

    if request.method == 'POST':
        form = OKRModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'OKR registered successfully!')
            form = OKRModelForm()
            status = 201
        else:
            messages.error(request, 'Error registering OKR!')
            status = 200

    return render(request, 'core/index.html', {'form': form}, status=status)
