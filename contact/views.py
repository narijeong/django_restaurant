from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

        try:
            send_mail(
                name + ' ' + phone, 
                message, 
                email, 
                ['narijeong@icloud.com']
            ) # subject, message, to, from
            
        except BadHeaderError:
            return HttpResponse('Invalid Header')

        return redirect('contact:send_sucess')

    
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)

def send_sucess(request):
    return HttpResponse("Youe message was sent!")