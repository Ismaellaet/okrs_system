from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseBadRequest

from .forms import ObjectiveModelForm, KeyResultModelForm
from .models import KeyResult


def registration(request):
    if request.method == 'POST':
        objective_form = ObjectiveModelForm(request.POST)
        kr_texts = request.POST.getlist('kr_text')

        try:
            if objective_form.is_valid() and kr_texts[0] != '':
                obj = objective_form.save()
                registered = register_krs(krs=kr_texts, objective=obj)

                if registered:
                    messages.success(request, 'OKR registered successfully!')
            else:
                raise Exception
        except Exception:
            print(1)
            messages.error(request, 'Error registering OKR!')
    context = {
        'objective_form': ObjectiveModelForm(),
        'kr_forms': create_kr_forms()
    }

    return render(request, 'core/index.html', context)


def register_krs(krs, objective):
    for kr_text in krs:
        if kr_text != '':
            kr = KeyResult(objective=objective, kr_text=kr_text)
            kr.save()
    return True


def create_kr_forms():
    kr_forms = [KeyResultModelForm() for i in range(5)]
    kr_forms[0].fields['kr_text'].required = True
    return kr_forms
