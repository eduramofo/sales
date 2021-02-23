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
    
    /* Paste btn [START] */
    $('#search-modal').find('#btn_search_query_group_addon').css('cursor', 'pointer');
    $('#search-modal').find('#btn_search_query_group_addon').click(function(e) {
        e.preventDefault();
        pasteTextFromClipboard(e);

    });
    const pasteTextFromClipboard = async (evt) => {
        const auth = await navigator.permissions.query({ name: "clipboard-read" });
        if (auth.state !== 'denied') {
            let text = await navigator.clipboard.readText();
            $('#search-modal').find('#id_search_query').val(text)
        }
    }
    /* Paste btn [END] */

});