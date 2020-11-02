"""sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.utils.translation import ugettext_lazy
from django.contrib.auth.views import LoginView
from leads.admin_custom import lead_admin_site


DEFAULT_TITLE = 'Wiser Sale'

admin.site.site_title  = ugettext_lazy(DEFAULT_TITLE)

admin.site.site_header = ugettext_lazy(DEFAULT_TITLE)

admin.site.index_title = ugettext_lazy(DEFAULT_TITLE)


urlpatterns = [
    
    path('admin/', admin.site.urls),

     path('admin-leads/', lead_admin_site.urls),

    path('accounts/login/', LoginView.as_view(
            template_name='admin/login.html',
            extra_context={
                'title': 'Login',
                'site_title': DEFAULT_TITLE,
                'site_header': DEFAULT_TITLE,
            },
        )
    ),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', include("core.urls")),

    path('', include("leads.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
