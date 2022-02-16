from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path(('api/users/'), include('users.urls')),
    path(('api/store/'), include('store.urls')),

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
admin.site.index_title = 'SimbaKids'
admin.site.site_title = 'SimbaKids.com'
admin.site.site_header = 'SimbaKids'