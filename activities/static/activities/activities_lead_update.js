$(document).ready(function() {

    var createNewActivityBtn = $('#create-new-activity-btn');
    
    createNewActivityBtn.click(createNewActivity);

    function createNewActivity(e) {
        e.preventDefault();
        var url = $(this).data('activities-add-activity-by-lead-url');
        $.get(url, function(modalHtml) {
            addActivityAddModalToDocument(modalHtml);
        });
    }

    function createNewActivity(e) {
        e.preventDefault();
        var url = $(this).data('activities-add-activity-by-lead-url');
        $.get(url, function(modalHtml) {
            addActivityAddModalToDocument(modalHtml);
        });
    }




    function addActivityAddModalToDocument(modalHtml) {
        var modal = $(modalHtml);
        addEventsListenersToActivityAddModal(modal);
        $('#nav-activity').append(modal);
        modal.modal('show');
    }

    function addEventsListenersToActivityAddModal(modal) {
        
    }

});
