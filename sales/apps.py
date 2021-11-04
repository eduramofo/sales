LOCAL_APPS = [
    'core.apps.CoreConfig',
    'leads.apps.LeadsConfig',
    'activities.apps.ActivitiesConfig',
    'integrations.apps.IntegrationsConfig',
    'analytics.apps.AnalyticsConfig',
    'academy.apps.AcademyConfig',
    'conversation.apps.ConversationConfig',
    'account.apps.AccountConfig',
    'signup.apps.SignupConfig',
    'login.apps.LoginConfig',
    'logout.apps.LogoutConfig',
    'event.apps.EventConfig',
]

THIRDS_APPS = [
    'widget_tweaks',
    'crispy_forms',
    'tempus_dominus',
    'rangefilter',
    'django_filters',
    # celery
    'django_celery_beat',
    'django_celery_results',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
]

APPS = LOCAL_APPS + THIRDS_APPS + DJANGO_APPS
