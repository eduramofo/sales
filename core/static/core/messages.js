$(document).ready(function() {

    var messagesIsProcessing = false;
    var delay = 2500;

    checkIfHasMessages();
    setInterval(checkIfHasMessages, 500);

    function checkIfHasMessages() {
        var messages = $('ul#django-messages li');        
        var hasMessages = messages.length;
        var notProcessing = !messagesIsProcessing;
        if(hasMessages && notProcessing) {
            messagesIsProcessing = true;
            processMessages(messages);
            setFinishProcessingMessages();
        }
    }
    
    function processMessages(messages) {
        var i;
        for (i = 0; i < messages.length;i++) {
            var message = messages[i];
            processMessage(message, i);
        }
    }

    function processMessage(message) {
        var messagesTemplates = $('#django-messages-toast-templates-wrapper');
        var toastsWrapper = messagesTemplates.find('#toasts-wrapper');
        var baseToast = toastsWrapper.find('.toast.base');
        createToast(baseToast, toastsWrapper, message);
    }

    function setFinishProcessingMessages() {
        setTimeout(function() {
            messagesIsProcessing = false;
            destroyAllMessages();
        }, delay + 500);
    }

    function destroyAllMessages() {
        $('#django-messages-toast-templates-wrapper').remove();
        $('#django-messages').remove();
    }

    function createToast(baseToast, toastsWrapper, message) {

        message = $(message);
        var tags = message.data('tags');
        var messageText = message.data('message');

        var headlineText = 'Notificação!';
        var headlineColorLabel = 'black';
        if (tags === 'success' ) {
            headlineText = 'Ação realizada com sucesso!';
            headlineColorLabel = 'green'; 
        }
        else if (tags === 'warning' ) { 
            headlineText = 'Alerta';
            headlineColorLabel = 'yellow'; 
        }
        else if (tags === 'debug' ) {    
            headlineColorLabel = 'orange'; 
        }
        else if (tags === 'info' ) {
            headlineColorLabel = 'blue';
        }
        else if (tags === 'error' ) {
            headlineText = 'Atenção! Houve algum erro na ação realizada.';
            headlineColorLabel = 'red';
        }

        var toast = baseToast.clone();
        toast.removeClass('base').removeClass('d-none');
        toast.find('.toast-header strong').text(headlineText);
        toast.find('.toast-body').text(messageText);
        toast.find('svg rect').attr('fill', headlineColorLabel);
        toast.appendTo(toastsWrapper);
        toast.toast({'delay': delay}).toast('show');
    }

});

(function (factory, jQuery, Zepto) {

    if (typeof define === 'function' && define.amd) {
        define(['jquery'], factory);
    } else if (typeof exports === 'object') {
        module.exports = factory(require('jquery'));
    } else {
        factory(jQuery || Zepto);
    }

} (function ($) {

$.fn.djangoMessages = function() {

    function success(data) {
        var messages = data.messages;
        if (messages) {
            insertDjangoMessagesInHtml(messages);
        }
    }

    function insertDjangoMessagesInHtml(messages) {
        $('body').prepend(messages);
    }

    var ajaxOptions = {
        type: "GET",
        url: '/messages/',
        success: success,
        dataType: 'json',
    }

    $.ajax(ajaxOptions);

}

}, window.jQuery, window.Zepto));
