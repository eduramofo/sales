$(document).ready(function() {
    var dueDateInput = $('form#event #id_start_datetime');
    setupDatetimePicker(dueDateInput);
});

function setupDatetimePicker(dateTimePickerInput) {
    dateTimePickerInput.datetimepicker({
        uiLibrary: 'bootstrap4',
        format: 'mm/dd/yyyy HH:MM',
        modal: true,
        showOnFocus: true,
        header: true,
        footer: true,
    });
};
