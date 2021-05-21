from django.contrib import admin

from academy import models as academy_models


@admin.register(academy_models.AudioSpeech)
class AudioSpeechAdmin(admin.ModelAdmin):

    search_fields = (
        'name',
    )

    list_display = (
        'active',
        'order',
        'name',
        'audio_file',
        'created_at',
        'updated_at',
    )
