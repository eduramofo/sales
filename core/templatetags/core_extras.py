from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.simple_tag
def btn_svg_icons(svg_group, icon_name, btn_text):

    icon_template_address = 'core/svg_icons/{}/{}.svg'.format(svg_group, icon_name)

    context = {
        'icon_template_address': icon_template_address,
        'btn_text': btn_text,
    }

    tlp_address = 'core/btn_svg_icons/entry.html'

    tlp_string = render_to_string(
        tlp_address,
        context,
    )

    tlp_safe = mark_safe(tlp_string)

    return tlp_safe
