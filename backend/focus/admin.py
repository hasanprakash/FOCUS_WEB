from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from focus.models import UpcomingEvents, Events, FocusTeam, Images, TechnologyClubs
# Register your models here.

class UpcomingEventsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class EventsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class FocusTeamAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class ImagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
class TechnologyClubsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(UpcomingEvents, UpcomingEventsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(FocusTeam, FocusTeamAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(TechnologyClubs, TechnologyClubsAdmin)