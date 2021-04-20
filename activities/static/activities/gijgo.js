
$(document).ready(function() {
    var dueDateInput = $('#id_activity-due_date')
    dueDateInput.datetimepicker({
        uiLibrary: 'bootstrap4',
        format: 'yyyy-mm-dd HH:MM',
        modal: false,
        showOnFocus: true,
        header: true,
        footer: true,
    });
});