from django.contrib import admin
import models

admin.site.register(models.Hardware)
admin.site.register(models.HardwareManufacturer)
admin.site.register(models.SoftwareChoices)
admin.site.register(models.HardwareChoices)
admin.site.register(models.Software)
