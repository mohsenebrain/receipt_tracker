# receipts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReceiptForm

def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipt_list.html', {'receipts': receipts})


def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    return render(request, 'receipts/receipt_detail.html', {'receipt': receipt})


def receipt_new(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.user = request.user
            receipt.save()
            messages.success(request, 'Receipt added successfully!')
            return redirect('receipt_detail', pk=receipt.pk)
    else:
        form = ReceiptForm()
    return render(request, 'receipts/receipt_edit.html', {'form': form})


def receipt_edit(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    if request.method == "POST":
        form = ReceiptForm(request.POST, instance=receipt)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.save()
            messages.success(request, 'Receipt updated successfully!')
            return redirect('receipt_detail', pk=receipt.pk)
    else:
        form = ReceiptForm(instance=receipt)
    return render(request, 'receipts/receipt_edit.html', {'form': form})


def receipt_delete(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    receipt.delete()
    messages.success(request, 'Receipt deleted successfully!')
    return redirect('receipt_list')
