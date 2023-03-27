from django.contrib import admin
from .models import Support

class SupportAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'name', 'subject', 'person', 'problem')
    list_display = ['name', 'subject', 'created_at','customer']
    search_fields = ['subject', 'name', 'person', 'problem']
    list_per_page = 10

    # Function to return Yes or No (customer)
    def customer(self, obj):
        if obj.person == 'Customer':
            return 'Yes'
        else:
            return 'No'
admin.site.register(Support, SupportAdmin)