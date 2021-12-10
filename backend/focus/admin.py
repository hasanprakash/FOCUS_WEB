from django.contrib import admin

from focus.models import UpcomingEvents, Events, FocusTeam, Images, TechnologyClubs
# Register your models here.

admin.site.register(UpcomingEvents)
admin.site.register(Events)
admin.site.register(FocusTeam)
admin.site.register(Images)
admin.site.register(TechnologyClubs)