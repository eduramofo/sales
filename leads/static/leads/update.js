$(document).ready(function() {

    $('button#leads-form-submit-btn').click(submitLeadForm);

    function submitLeadForm(e) {
        e.preventDefault();
        $('form#leads').submit();
    }

    pageActions();

    //setupAndNow();

    function pageActions() {

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
            window.location.href = waHref;
            openInNewTab(waHref);
        } else if (action === 'call') {
            window.location.href = callHref;
        }

    }

    function setupAndNow() {
        url = new URL(window.location.href);
        const andNow = url.searchParams.get('and-now')
        const andNowT1Modal = $('#and-now-t1-modal');
        if (andNow === 't2') {
            andNowT1Modal.modal('show');
            countDown(5, andNowT1Modal.find('#countdown'));
        };
    };

    function countDown(duration, display) {
        var timer = duration, minutes, seconds;
        duration = duration * 60;
        setInterval(function () {
            minutes = parseInt(timer / 60, 10);
            seconds = parseInt(timer % 60, 10);
            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;
            display.text(minutes + ":" + seconds);
            if (--timer < 0) {
                timer = duration;
            }
        }, 1000);
    };










});
