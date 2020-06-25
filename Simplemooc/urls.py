from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()



urlpatterns = [
    path('', include('Simplemooc.core.urls', namespace='core')),
    path('conta/', include('Simplemooc.accounts.urls', namespace='accounts')),
    path('cursos/', include('Simplemooc.courses.urls', namespace='courses')),
    path('forum/', include('Simplemooc.forum.urls', namespace='forum')),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)


