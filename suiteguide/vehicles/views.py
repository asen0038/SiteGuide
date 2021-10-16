from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm


def create(request):

    context = {}

    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create.html", context)


def listAll(request):

    context = {"dataset": Vehicle.objects.all()}

    return render(request, "list.html", context)


def update(request, id):

    context = {}

    vehicle = get_object_or_404(Vehicle, id=id)

    form = VehicleForm(request.POST or None, instance=vehicle)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["form"] = form

    return render(request, "update.html", context)


def delete(request, id):

    context = {}

    obj = get_object_or_404(Vehicle, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete.html", context)
