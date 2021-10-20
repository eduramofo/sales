$(document).ready(function() {
    setupFilter();
});

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
