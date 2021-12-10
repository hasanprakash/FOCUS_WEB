from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from focus import views

from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()
router.register(r'upcomingevents', views.UpcomingEventsViewSet)
router.register(r'events', views.EventsViewSet)
router.register(r'focusteam', views.FocusTeamViewSet)
router.register(r'gallery', views.ImagesViewSet)
router.register(r'techclubs', views.TechnologyClubsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
