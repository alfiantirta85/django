from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Catering(models.Model):
    nama = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="min 8 digit")
    telpon = models.CharField(validators=[phone_regex],max_length=15,blank=True)
    alamat = models.TextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.nama
    
class Makanan(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.IntegerField()
    gambar = models.ImageField(upload_to='menu/images/')
    keterangan = models.TextField(blank=True,null=True)
    stok = models.IntegerField()
    catering = models.ForeignKey(Catering,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nama
    
class Minuman(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.IntegerField()
    gambar = models.ImageField(upload_to='menu/images/')
    keterangan = models.TextField(blank=True,null=True)
    stok = models.IntegerField()
    catering = models.ForeignKey(Catering,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nama
    
class CartItem(models.Model):
    makanan = models.ForeignKey(Makanan, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)