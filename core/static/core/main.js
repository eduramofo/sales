$(document).ready(function() {

    $('a#search-call-modal-btn').click(function(e) {
        e.preventDefault();
        $('#search-modal').modal('show');
    });

    $('#search-modal').on('shown.bs.modal', function(e) {
        $(this).find('#id_search_query').focus();
    });

    $('#search-modal').find("#search-modal-clear-btn").click(function(e) {
        e.preventDefault();
        $('#search-modal').find('#id_search_query').val('').focus();
    });

});