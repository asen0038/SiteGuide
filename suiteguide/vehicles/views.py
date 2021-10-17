from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm
from django.views import View


class Create(View):
    form_class = VehicleForm
    context = {'key': 'value'}
    template = 'create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.context)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template, {'form': form})


class ListAll(View):

    def get(self, request):
        context = {"dataset": Vehicle.objects.all()}
        return render(request, "list.html", context)


class Update(View):
    form_class = VehicleForm
    context = {'key': 'value'}
    template = 'update.html'

    def get(self, request, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, id=kwargs.get('id'))
        form = self.form_class(instance=vehicle)
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, id=kwargs.get('id'))
        form = self.form_class(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")


class Delete(View):
    context = {'key': 'value'}
    template = 'delete.html'

    def get(self, request, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, id=kwargs.get('id'))
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs):
        vehicle = get_object_or_404(Vehicle, id=kwargs.get('id'))
        vehicle.delete()
        return HttpResponseRedirect("/")
