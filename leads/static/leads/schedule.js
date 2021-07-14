$(document).ready(function() {

    var scheduleBtnConversation = $('#schedule-conversation-modal-btn');

    var scheduleBtnDirect = $('#schedule-direct-modal-btn');

    scheduleBtnConversation.click(function(e) {
        e.preventDefault();
        getScheduleConversation($(this));
    });

    scheduleBtnDirect.click(function(e) {
        e.preventDefault();
        getScheduleDirect($(this));
    });

    function getScheduleConversation(scheduleBtn) {

        var url = scheduleBtn.data('url');

        $.get(url, success);

        function success(resp) {

            var scheduleModal = $(resp);
            var dueDateInput = scheduleModal.find('#id_due_date');
            var formConfirmBtn = scheduleModal.find('#schedule-modal-confirm-btn');
            
            setupDatetimePicker(dueDateInput);
            
            formConfirmBtn.click(function(e) {    
                e.preventDefault();
                formSubmit(scheduleModal, url);
            });

            appendScheduleModalToBody(scheduleModal);

            closeConversionModal();

            showScheduleModal(scheduleModal);

            scheduleModal.on('hidden.bs.modal', function() {
                destroyScheduleModal(scheduleModal);
            });

        };

    };

    function getScheduleDirect(scheduleBtn) {

        var url = scheduleBtn.data('url');

        $.get(url, success);

        function success(resp) {

            var scheduleModal = $(resp);
            var dueDateInput = scheduleModal.find('#id_due_date');
            var formConfirmBtn = scheduleModal.find('#schedule-modal-confirm-btn');
            
            setupDatetimePicker(dueDateInput);
            
            formConfirmBtn.click(function(e) {    
                e.preventDefault();
                formSubmit(scheduleModal, url);
            });

            appendScheduleModalToBody(scheduleModal);

            closeAttemptModal();

            showScheduleModal(scheduleModal);

            scheduleModal.on('hidden.bs.modal', function() {
                destroyScheduleModal(scheduleModal);
            });

        };

    };

    function setupDatetimePicker(dateTimePickerInput) {

        dateTimePickerInput.datetimepicker({
            uiLibrary: 'bootstrap4',
            format: 'yyyy-mm-dd HH:MM',
            modal: false,
            showOnFocus: true,
            header: true,
            footer: true,
        });

    };

    function formSubmit(modal, url) {

        var form = modal.find('#schedule-modal-form');
        
        var data = form.serialize();

        var ajaxOption = {
            url: url,
            method: 'post',
            data: data,
            success: success,
        };

        $.ajax(ajaxOption);
        
        function success(content) {
            var newContent = $(content);
            var newModalContent = newContent.find('.modal-content');
            modal.find('.modal-dialog').empty();
            modal.find('.modal-dialog').off();
            modal.find('.modal-dialog').append(newModalContent);
        };
        
    };

    function appendScheduleModalToBody(modal) {
        $('body').append(modal);
    };

    function showScheduleModal(modal) {
        modal.modal();
    };

    function destroyScheduleModal(modal) {
        modal.remove();
        location.reload();
    };

    function closeConversionModal() {
        $('#conversation-modal').modal('hide');
    };
    
    function closeAttemptModal() {
        $('#attempts-modal').modal('hide');
    };

});