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


class SubmoduleInline(admin.TabularInline):
    model = academy_models.Submodule
    extra = 0


@admin.register(academy_models.Module)
class ModuleAdmin(admin.ModelAdmin):

    search_fields = (
        'title',
    )

    list_display = (
        'active',
        'title',
        'url',
        'order',
    )

    inlines = [SubmoduleInline]


@admin.register(academy_models.Submodule)
class SubmoduleAdmin(admin.ModelAdmin):

    search_fields = (
        'title',
    )

    list_display = (
        'active',
        'title',
        'url',
        'order',
    )

    autocomplete_fields = ['module']
