from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'home/thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form':form})