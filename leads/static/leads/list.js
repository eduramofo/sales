$(document).ready(function() {

    var leadTable = $('table#lead-table-list');

    // filter btn
    $('#filter-toggle-btn').click(function(e) {
        e.preventDefault();
        $('#filter-form-wrapper').toggleClass('d-none');
    });

    // now - START
    leadTable.find('tbody tr td.run-now-td').css('cursor', 'pointer').click(changeLeadRunNowStatus);
    function changeLeadRunNowStatus (e) {
        
        var currentTd = $(this);
        
        var ajaxOptions = {
            type: "POST",
            url: currentTd.data('run-now-url'),
            headers: {'X-CSRFToken': Cookies.get('csrftoken')},
            data: currentTd.data('run-now-data'),
            success: success,
            dataType: 'json',
        }

        function success(data) {
            if (data.success) {
                var newTd = $(data.td_html[0]);
                var newTdData =  newTd.data('run-now-data');
                var newTdUrl =  newTd.data('run-now-url');
                var newTdHtml =  newTd.html();
                currentTd.data('run-now-data', newTdData);
                currentTd.data('run-now-url', newTdUrl);
                currentTd.html(newTdHtml);

            } else {
                console.log('Ocorreu algum erro desconhecido, atualize a página e tente novamente.');
            }
        }

        $.ajax(ajaxOptions);

    }
    // now - END

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