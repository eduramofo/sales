$(document).ready(function() {

    $('button#leads-form-submit-btn').click(submitLeadForm);

    function submitLeadForm(e) {
        e.preventDefault();
        $('form#leads').submit();
    }


    (function pageActions() {

        var action = getParameterByName('action');
        var waHref = $('#leads-call-whatsapp-sc-btn').prop('href');
        var callHref = $('#leads-call-phone-sc-btn').prop('href');

        function getParameterByName(name, url = window.location.href) {
            name = name.replace(/[\[\]]/g, '\\$&');
            var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
                results = regex.exec(url);
            if (!results) return null;
            if (!results[2]) return '';
            return decodeURIComponent(results[2].replace(/\+/g, ' '));
        }

        function openInNewTab(url) {
            window.open(url, '_blank');
        }

        if (action === 'wa') {
            openInNewTab(waHref);
        } else if (action === 'call') {
            openInNewTab(callHref);
        }

    })();

});
