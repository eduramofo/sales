from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import ugettext_lazy

DEFAULT_TITLE = 'Sales Up'

admin.site.site_title  = ugettext_lazy(DEFAULT_TITLE)

admin.site.site_header = ugettext_lazy(DEFAULT_TITLE)

admin.site.index_title = ugettext_lazy(DEFAULT_TITLE)


urlpatterns = [
    
    path('', include('core.urls')),
    
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('login/', include('login.urls')),

    path('leads/', include('leads.urls.main')),

    path('integrations/', include('integrations.urls')),

    path('analytics/', include('analytics.urls')),

    path('activities/', include('activities.urls')),

    path('event/', include('event.urls')),

    path('signup/', include('signup.urls')),

    path('academy/', include('academy.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
