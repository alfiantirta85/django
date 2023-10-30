from django.db import models

# Create your models here.
class Pasien(models.Model):
    nama = models.CharField(max_length=250)
    nomor_rekam_medis = models.CharField(max_length=250)
    alamat = models.CharField(max_length=250)
    jenis_kelamin = models.CharField(max_length=250)
    tanggal_lahir = models.DateField()
    dokter = models.CharField(max_length=250)
    departemen = models.CharField(max_length=250)
    diagnosa = models.CharField(max_length=250)
    nomor_ruangan = models.CharField(max_length=250)
    jam = models.TimeField()
    tindakan = models.CharField(max_length=250)
    keterangan = models.TextField(blank=True,null=True)
    def __str__(self) -> str:
        return self.nama