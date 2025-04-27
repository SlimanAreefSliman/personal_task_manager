from django.urls import path, include
from django.conf import settings
from django.contrib import admin  # Add admin import
from tasks.views import homepage
#======================================
urlpatterns = [
path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),  # Add admin URLs
    path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
