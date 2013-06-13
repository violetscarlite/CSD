from django.contrib import admin
from csd_app import models

admin.site.register(models.Team)
admin.site.register(models.UserProfile)
admin.site.register(models.GeneralTeamData)
admin.site.register(models.Competition)
admin.site.register(models.Regional)
admin.site.register(models.Robot)
admin.site.register(models.TeamDataSetup)
admin.site.register(models.Match)
admin.site.register(models.Alliance)
admin.site.register(models.DataGroup)
admin.site.register(models.DataSetup)
admin.site.register(models.DataModel)