from django.contrib import admin
from .models import Doctor, Malade


admin.site.site_header='hope card'
admin.site.site_header='hope card'
class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['id_docteur']
    list_display=['nom','id_docteur','specialite']
admin.site.register(Doctor, DoctorAdmin)
class MAladeAdmin(admin.ModelAdmin):
    search_fields = ['numero_identite']
    list_display=['nom','prenom','numero_identite']
admin.site.register(Malade, MAladeAdmin)