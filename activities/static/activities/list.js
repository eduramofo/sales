$(document).ready(function() {

    // filter btn
    $('#filter-toggle-btn').click(function(e) {
        e.preventDefault();
        $('#filter-form-wrapper').toggleClass('d-none');
    });

    // pagination - START
    var navPagination = $('nav.pagination ul.pagination');
    navPagination.find('li.page-item:not(.disabled,.not-clickable)').click(pagination);
    navPagination.find('a').click(function (e) {e.preventDefault();});

    function pagination(e) {

        e.preventDefault();
        var pageNumber = $(this).find('a').data('page-number');

        if (pageNumber) {
            insertParam('page', pageNumber);
        }

        function insertParam(key, value) {

            key = encodeURI(key); value = encodeURI(value);

            var kvp = document.location.search.substr(1).split('&');

            var i=kvp.length; var x; while(i--)
            {
                x = kvp[i].split('=');

                if (x[0]==key)
                {
                    x[1] = value;
                    kvp[i] = x.join('=');
                    break;
                }
            }

            if(i<0) {kvp[kvp.length] = [key,value].join('=');}

            //this will reload the page, it's likely better to store this until finished
            document.location.search = kvp.join('&');
        }

    }
    // pagination - END

});