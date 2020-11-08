from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage


def make_paginator(request, qs_filter, size):
    paginator = Paginator(qs_filter, size)
    try:
        page = paginator.page(request.GET.get('page'))
    except (InvalidPage, PageNotAnInteger):
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    index = page.number
    range_size = 5
    max_index = len(paginator.page_range)
    start_index = index - range_size if index >= range_size else 0
    end_index = index + range_size if index <= max_index - range_size else max_index
    page_range = paginator.page_range[start_index:end_index]

    page_data = {
        'page': page,
        'page_range': page_range,
    }
    return page_data
