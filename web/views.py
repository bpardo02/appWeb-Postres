from django.shortcuts import render
from .models import Flan, ContactForm, FavoriteFlan
from .forms import ContactFormModelForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flanes": flanes_publicos})


def about(request):
    return render(request, "about.html")


@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)

    return render(request, "welcome.html", {"flanes": flanes_privados})


def contact(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactFormModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/exito")
    else:
        # if a GET (or any other method) we'll create a blank form
        form = ContactFormModelForm()

    return render(request, "contact.html", {"form": form})


def exito(request):
    return render(request, "exito.html")


@login_required
def toggle_favorite_flan(request, flan_uuid):
    flan = get_object_or_404(Flan, flan_uuid=flan_uuid)
    favorite, created = FavoriteFlan.objects.get_or_create(user=request.user, flan=flan)

    if not created:
        favorite.delete()
    return redirect("flan_detail", flan_uuid=flan_uuid)


def flan_detail(request, flan_uuid):
    flan = get_object_or_404(Flan, flan_uuid=flan_uuid)
    is_favorited = False
    if request.user.is_authenticated:
        is_favorited = FavoriteFlan.objects.filter(
            user=request.user, flan=flan
        ).exists()

    return render(
        request,
        "flan_detail.html",
        {
            "flan": flan,
            "is_favorited": is_favorited,
        },
    )


@login_required
def favorite_flans(request):
    favoritos = FavoriteFlan.objects.filter(user=request.user).select_related("flan")
    return render(request, "favorite_flans.html", {"favoritos": favoritos})
