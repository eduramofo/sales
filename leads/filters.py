from leads.models import Lead
import django_filters


class LeadFilter(django_filters.FilterSet):    
    
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    indicated_by_contains = django_filters.CharFilter(field_name='indicated_by', lookup_expr='icontains')
    indicated_by_exact = django_filters.CharFilter(field_name='indicated_by', lookup_expr='iexact')
    tel = django_filters.CharFilter(field_name='tel', lookup_expr='icontains')
    waid = django_filters.CharFilter(field_name='waid', lookup_expr='icontains')

    class Meta:
        model = Lead
        fields = ['name', 'indicated_by', 'tel','waid',]
