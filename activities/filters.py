import django_filters

from activities.models import Activity


class ActivityFilter(django_filters.FilterSet):

    class Meta:
        model = Activity
        fields = '__all__'
        order_by_field = 'quality'
