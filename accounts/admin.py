from django.contrib import admin
from accounts.models import UserProfile, Accounts, Transactions
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Accounts)
admin.site.register(Transactions)