from django.contrib import admin
from .models import Catering
from .models import Makanan
from .models import Minuman

# Register your models here.
admin.site.register(Catering)
admin.site.register(Makanan)
admin.site.register(Minuman)