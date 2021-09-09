$(document).ready(function() {
    setupDatetimePicker();
    setupFilter();
});

function setupDatetimePicker() {
    var dueDateInput = $('form#event #id_start_datetime');
    if(dueDateInput.length) {
        dueDateInput.datetimepicker({
            uiLibrary: 'bootstrap4',
            format: 'mm/dd/yyyy HH:MM',
            modal: true,
            showOnFocus: true,
            header: true,
            footer: true,
        });
    };
};

function setupFilter() {

    var eventFilterWrapperBtn = $('button#event-filter-wrapper-btn');
    var eventFilterWrapperContent = $('#event-filter-wrapper-content');
    
    if(eventFilterWrapperBtn.length) {
        eventFilterWrapperBtn.click(function(e) {
            e.preventDefault();
            toggleContent();
        });
    };

    function toggleContent() {
        eventFilterWrapperBtn.attr('disabled', true);
        if (eventFilterWrapperContent.attr("class").split(' ').includes('d-none')) {
            showContent();
        } else {
            hideContent();
        };
        eventFilterWrapperBtn.attr('disabled', false);
    };

    function showContent() {
        eventFilterWrapperBtn.text('Esconder Filtro');
        eventFilterWrapperContent.removeClass('d-none');
    };

    function hideContent() {
        eventFilterWrapperBtn.text('Mostrar Filtro');
        eventFilterWrapperContent.addClass('d-none');
    };

};
