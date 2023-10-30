from django.shortcuts import render, redirect
from .models import Makanan
from .models import Minuman
from .models import CartItem
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    searchMakanan = request.GET.get('nama')
    if searchMakanan:
        makanans = Makanan.objects.filter(nama__icontains=searchMakanan)
    else:
        makanans = Makanan.objects.all()
    return render(request,'home.html',{'searchMakanan':searchMakanan,'makanans':makanans})

def detail(request,makanan_id):
    makanan = get_object_or_404(Makanan,pk=makanan_id)
    return render(request,'detail.html',{'makanan':makanan})

def minuman(request):
    searchMinuman = request.GET.get('nama')
    if searchMinuman:
        minumans = Minuman.objects.filter(nama__icontains=searchMinuman)
    else:
        minumans = Minuman.objects.all()
    return render(request,'minuman.html',{'searchMinuman':searchMinuman,'minumans':minumans})

def detail_minuman(request,minuman_id):
    minuman = get_object_or_404(Minuman,pk=minuman_id)
    return render(request,'detailminum.html',{'minuman':minuman})

def add_to_cart(request, makanan_id):
    makanan_id = int(makanan_id)
    makanan = Makanan.objects.get(pk=makanan_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1)) # Jumlah pesanan dari form
        if quantity < 1:
            quantity = 1 # Minimal 1
        if makanan.stok >= quantity:
        # Char_item jika sudah ada pesanan makanan tersebut
        # Created jika belum ada pesanan makanan tersebut maka disimpan dan create += true
            cart_item, created = CartItem.objects.get_or_create(makanan=makanan)
        # If the item exists, update the quantity anda item_total
            if not created:
                cart_item.quantity += quantity
                cart_item.item_total = cart_item.quantity * makanan.harga
                cart_item.save()
            else:
                cart_item.quantity = quantity
                cart_item.item_total = quantity * makanan.harga
                cart_item.save()
            makanan.stok -= quantity
            makanan.save()
        else:
            messages.error(request, 'Stok habis untuk makanan ' + makanan.nama)
    return redirect('cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.item_total for item in cart_items)
    nama = request.GET.get('nama')
    telp = request.GET.get('telp')
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'nama': nama, 'telp': telp })

def remove_from_cart(request, makanan_id):
    makanan_id = int(makanan_id)
    makanan = Makanan.objects.get(pk=makanan_id)
    try:
        cart_item = CartItem.objects.get(makanan=makanan)
        cart_item.delete()
        messages.success(request, 'Pesanan berhasil dihapus')
    except CartItem.DoesNotExist:
        messages.warning(request, 'Pesanan tidak ditemukan')
    return redirect('cart')