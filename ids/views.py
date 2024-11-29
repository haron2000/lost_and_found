from django.shortcuts import render, redirect
from .forms import LostFoundIDForm
from .forms import SearchIDForm
from .models import LostFoundID

def landing_page(request):
    return render(request, 'ids/landing.html')
def report_id(request):
    if request.method == 'POST':
        form = LostFoundIDForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = LostFoundIDForm()
    return render(request, 'ids/report_id.html', {'form': form})

def success(request):
    return render(request, 'ids/success.html')

def search_id(request):
    form = SearchIDForm()
    results = None

    if request.method == 'POST':
        form = SearchIDForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data['id_number']
            # Search for lost or found IDs that match the input ID number
            results = LostFoundID.objects.filter(id_number=id_number)
    
    return render(request, 'ids/search_id.html', {'form': form, 'results': results})

