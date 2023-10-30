from django.contrib import admin
from .models import Toko
from .models import Barang

# Register your models here.
admin.site.register(Toko)
admin.site.register(Barang)