from django.contrib import admin
from receipts.models import Receipt


class ReceiptAdmin(admin.ModelAdmin):
    pass


admin.site.register(Receipt, ReceiptAdmin)