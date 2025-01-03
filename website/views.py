from django.shortcuts import render,HttpResponseRedirect,reverse
from website.models import Contact
from website.forms import ContactForm,NameForm,NewsletterForm
from django.http import HttpResponse,JsonResponse
from django.contrib import messages

def index_view(request):
    return render(request,("website/index.html"))

def about_view(request):
    return render(request,("website/about.html"))

def contact_view(request):
    if request.method == "POST":
        request.POST = request.POST.copy()
        request.POST['name'] = 'Unknown'
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Your messages submitted successfully")
        else:
            messages.add_message(request,messages.ERROR,"Your messages did not submit correctly")
    form = ContactForm()
    return render(request,("website/contact.html"),{'form':form})

def elements_view(request):
    return render(request,("website/elements.html"))

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('website:index'))
    else:
        return HttpResponseRedirect(reverse('website:index'))

def test1_view(request):
    c = Contact()
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            c.name=form.cleaned_data["name"]
            c.email=form.cleaned_data["email"]
            c.subject=form.cleaned_data["subject"]
            c.message=form.cleaned_data["message"]
            c.save()
            print(c.name,c.email,c.subject,c.message)
            return HttpResponse("done")   
        else:
            return HttpResponse("error")
    form = NameForm()
    return render(request,("test1.html"),{'form':form})