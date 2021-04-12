$(document).ready(function() {

    var scheduleBtn = $('#schedule-modal-btn');

    scheduleBtn.click(function(e) {
        e.preventDefault();
        get();
    });

    function get() {
        
        var url = scheduleBtn.data('url');
        
        $.get(url, success);

        function success(resp) {
            
            var scheduleModal = $(resp);
            var dueDateInput = scheduleModal.find('#id_due_date');
            var form = scheduleModal.find('#schedule-modal-form');
            var formConfirmBtn = form.find('#schedule-modal-confirm-btn');

            dueDateInput.datetimepicker({
                uiLibrary: 'bootstrap4',
                format: 'yyyy-mm-dd HH:MM',
                modal: false,
                footer: true
            });

            formConfirmBtn.click(function(e) {
                
                e.preventDefault();
                
                var data = form.serialize();
                
                var url = form.attr('action');

                var ajaxOption = {
                    url: url,
                    method: 'post',
                    data: data,
                    success: success,
                }
                
                $.ajax(ajaxOption);
                
                function success(content) {
                    var newContent = $(content);
                    var newModalContent = newContent.find('.modal-content');
                    scheduleModal.find('.modal-dialog').empty();
                    scheduleModal.find('.modal-dialog').off();
                    // initForm(newModalContent);
                    // var formIsValid = true;
                    // formIsValid = !newContent.find('ul#django-messages').html().includes('data-tags="error"');
                    // modalMessages(content, newModalContent);
                    scheduleModal.find('.modal-dialog').append(newModalContent);
                }

            });
            
            $('body').append(scheduleModal);
            
            scheduleModal.modal();
        }

    };

});