from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.forms import SubscribeForm

# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            return redirect(reverse('thank_you'))
    
    context = {'form':subscribe_form}
    return render(request,'subscribe/subscribe.html',context)

def thank_you(request):
    return render(request,'subscribe/thank_you.html',{})
