from django.contrib import admin
from .models import RevolvingDoor


class RevolvingDoorAdmin(admin.ModelAdmin):
    list_display = ['crm_no', 'company','mr30_type','published_date']
    list_display_links = ['crm_no', 'company','mr30_type','published_date']
    search_fields = ['crm_no', 'company','mr30_type','published_date']
    list_filter = ['crm_no', 'company','mr30_type','published_date']

    class Meta:
        model = RevolvingDoor

admin.site.register(RevolvingDoor,RevolvingDoorAdmin)
