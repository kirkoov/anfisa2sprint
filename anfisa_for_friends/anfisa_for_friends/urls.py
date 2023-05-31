from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('ice_cream/', include('ice_cream.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar  # type: ignore[import]
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
