$(document).ready(function() {

    $('button#leads-form-submit-btn').click(submitLeadForm);

    function submitLeadForm(e) {
        e.preventDefault();
        $('form#leads').submit();
    }

});
