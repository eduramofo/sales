from leads.models import Lead, LEAD_STATUS_CHOICES
import django_filters


class LeadFilter(django_filters.FilterSet):    

    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    indicated_by_contains = django_filters.CharFilter(field_name='indicated_by', lookup_expr='icontains')
    indicated_by_exact = django_filters.CharFilter(field_name='indicated_by', lookup_expr='iexact')
    tel = django_filters.CharFilter(field_name='tel', lookup_expr='icontains')
    waid = django_filters.CharFilter(field_name='waid', lookup_expr='icontains')

    # status
    status = django_filters.ChoiceFilter(choices=LEAD_STATUS_CHOICES)

    # quality
    quality_gte = django_filters.NumberFilter(field_name='quality', lookup_expr='gte')
    quality_lte = django_filters.NumberFilter(field_name='quality', lookup_expr='lte')

    # next contact
    next_contact_gte = django_filters.DateTimeFilter(field_name='next_contact', lookup_expr='gte')
    next_contact_lte = django_filters.DateTimeFilter(field_name='next_contact', lookup_expr='lte')

    class Meta:
        model = Lead
        fields = ['name', 'status', 'indicated_by', 'tel', 'waid', 'quality', 'next_contact']
        order_by_field = 'quality'
