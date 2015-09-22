from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

from HelloWorld.models import HelloWorld
# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

class HelloWorldForm(ModelForm):
    class Meta:
        model = HelloWorld
        fields = ['name', 'ip', 'order']

def HelloWorld_list(request,template_name='HelloWorld/HelloWorld_list.html'):
    HelloWorld= HelloWorld.objects.all()
    data = {}
    data['object_list'] = HelloWorld
    return render(request, template_name, data)

def HelloWorld_create(request,template_name='HelloWorld/HelloWorld_list.html'):
    form = HelloWorldForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('HelloWorld_list')
    return render(request,template_name, {'form':form})

def HelloWorld_update(request, pk, template_name='HelloWorld/HelloWorld_form.html'):
    HelloWorld = get_object_or_404(HelloWorld, pk=pk)
    form = HelloWorldForm(request.POST or None, instance=HelloWorld)
    if form.is_valid():
        form.save()
        return redirect('HelloWorld_list')
    return render(request, template_name, {'form':form})

def HelloWorld_delete(request, pk, template_name='HelloWorld/HelloWorld_confirm_delete.html'):
    HelloWorld = get_object_or_404(HelloWorld, pk=pk)
    if request.method=='POST':
        HelloWorld.delete()
        return redirect('HelloWorld_list')
    return render(request, template_name, {'object':HelloWorld})


class HelloWorldList(ListView):
    model = HelloWorld

class HelloWorldCreate(CreateView):
    model = HelloWorld
    success_url = reverse_lazy('HelloWorld_list')
    fields = ['name', 'ip', 'order']

class HelloWorldUpdate(UpdateView):
    model = HelloWorld
    success_url = reverse_lazy('HelloWorld_list')
    fields = ['name', 'ip', 'order']

class HelloWorldDelete(DeleteView):
    model = HelloWorld
    success_url = reverse_lazy('HelloWorld_list')
