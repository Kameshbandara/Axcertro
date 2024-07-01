from django.shortcuts import get_object_or_404, redirect, render

from .forms import detailForm
from .models import details


def Home(request):
    form = detailForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'Home.html', {'form': form})


def list(request):
    alldetails = details.objects.all()
    return render(request, 'list.html', {'details': alldetails})


def update(request, pk):
    detail = get_object_or_404(details, pk=pk)
    form = detailForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('details-list')
    return render(request, 'update.html', {'form': form})


def delete(request, pk):
    detail_instance = get_object_or_404(details, pk=pk)
    
    if request.method == 'POST':
        detail_instance.delete()
        return redirect('details-list')
    
    return render(request, 'delete.html', {'detail_instance': detail_instance})