from django.shortcuts import get_object_or_404, render

from .models import Dorama
from . import tasks
from . import forms

def list_view(request):
    if request.method == "POST":
        tasks.parsing.delay(request.POST.get("page"))
    form = forms.PageForm()
    return render(request,"dorama/list.html",{
        "page_form": form,
        "card_list": Dorama.objects.all(),
    })


def detail_view(request, pk):
    obj = get_object_or_404(Dorama, pk=pk)
    return render(
        request,
        "dorama/detail.html",
        {
            "object": obj
        })