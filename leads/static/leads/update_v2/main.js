$(document).ready(function() {

    var baseUrl = '';

    var url_string = window.location;
    var url = new URL(url_string);
    var leadId = url.searchParams.get("id");

    startUpPage(leadId);

    function startUpPage(leadId) {
        var lead_url = baseUrl + leadId + '/';
        console.log(lead_url);
        $.get(lead_url, success);
        function success(resp) {
            insertRespInPage(resp);
        }
    }

    function insertRespInPage(resp) {
        var $resp = $(resp);
        $('body').append($resp);
    }













});
