from django.contrib import admin

# Register your models here.
from .models import P_admin
admin.site.register(P_admin)

from .models import P_product
admin.site.register(P_product)

from .models import P_user
admin.site.register(P_user)

from .models import cart
admin.site.register(cart)
