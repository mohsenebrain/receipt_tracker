# receipts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Receipt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReceiptForm
@login_required()
def receipt_list(request):
    receipts = Receipt.objects.filter(user=request.user)
    return render(request, 'receipt_list.html', {'receipts': receipts})

@login_required()
def receipt_detail(request, pk):
    # receipt = get_object_or_404(Receipt, pk=pk)
    # return render(request, 'receipt_detail.html', {'receipt': receipt})
    context = {}
    receipt = Receipt.objects.get(pk = pk)
    if request.user.id == receipt.user.id:
        context['receipt'] = receipt
        return render(request, 'receipt_detail.html', context)
    return redirect('receipt_list')
@login_required(login_url="")
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
    return render(request, 'receipt_edit.html', {'form': form})

@login_required(login_url="")
def receipt_edit(request, pk):
    # receipt = get_object_or_404(Receipt, pk=pk)
    # if request.method == "POST":
    #     form = ReceiptForm(request.POST, instance=receipt)
    #     if form.is_valid():
    #         receipt = form.save(commit=False)
    #         receipt.save()
    #         messages.success(request, 'Receipt updated successfully!')
    #         return redirect('receipt_detail', pk=receipt.pk)
    # else:
    #     form = ReceiptForm(instance=receipt)
    # return render(request, 'receipt_edit.html', {'form': form})

    receipt = Receipt.objects.get(pk = pk)
    if request.user.id == receipt.user.id:
        form = ReceiptForm(instance=receipt)
        if request.method == 'POST':
            form = ReceiptForm(request.POST, instance=receipt)
            if form.is_valid():
                form.save()
                return redirect('receipt', pk=receipt.pk)
        context = {'form':form}
        return render(request, 'receipt_edit.html', context)
    return redirect('receipt_list')

# @login_required(login_url="")
# def receipt_delete(request, pk):
#     receipt = get_object_or_404(Receipt, pk=pk)
#     receipt.delete()
#     messages.success(request, 'Receipt deleted successfully!')
#     return redirect('receipt_list')

@login_required(login_url='')
def receipt_delete(request, pk):
    receipt = Receipt.objects.get(pk=pk)
    if request.user.id == receipt.user.id:
        receipt.delete()
        messages.success(request, 'Receipt deleted successfully!')
        return redirect('receipt_list')
    return redirect('receipt_list')

##delete the logged in user account
# @login_required(login_url='login')
# def deleteUser(request):
#     user = request.user
#     user.delete()
#     return redirect('login')