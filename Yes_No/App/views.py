from django.shortcuts import render
from .forms import SupportForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Home
def home(request):
    form = SupportForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Request sent successfully !')
        return HttpResponseRedirect('/')
    context = {"form": form}
    return render(request, "home.html", context)