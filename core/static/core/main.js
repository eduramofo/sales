$(document).ready(function() {

    // checkForDjMessages
    (function checkForDjMessages() {

        var messagesIsProcessing = false;

        setInterval(checkMessages, 60);

        function checkMessages() {

            var djMessages = $('div#dj-messages');

            if(djMessages.length && messagesIsProcessing === false) {

                messagesIsProcessing = true;

                djMessages.find('.message-item').each(function () {
                    if ($(this).data('processed') === false) {
                        var message = $(this).data('message');
                        var tag = $(this).data('tag');
                        showAlertToast(tag, message);
                    }
                });

                djMessages.remove();

                messagesIsProcessing = false;
            }

        }

    })();

    function showAlertToast(alertType, messageMainText) {
        
        var headlineText = 'Notificação!';
        
        var headlineColorLabel = 'black';

        if      ( alertType === 'success' ) {
            headlineText = 'Ação realizada com sucesso!';
            headlineColorLabel = 'green'; 
        }

        else if ( alertType === 'warning' ) { 
            headlineText = 'Alerta';
            headlineColorLabel = 'yellow'; 
        }
        
        else if ( alertType === 'debug' ) {
             
            headlineColorLabel = 'orange'; 
        }
        
        else if ( alertType === 'info' ) {
            headlineColorLabel = 'blue';
        }
        
        else if ( alertType === 'error' ) {
            headlineText = 'Atenção! Houve algum erro na ação realizada.';
            headlineColorLabel = 'red';
        }

        var alertContent    = '<div class="toast" role="alert"'
        alertContent        = alertContent + 'aria-live="assertive" aria-atomic="true"><div class="toast-header"><svg class="bd-placeholder-img rounded mr-2"'
        alertContent        = alertContent + 'width="20" height="20" xmlns="http://www.w3.org/2000/svg"'
        alertContent        = alertContent + 'preserveAspectRatio="xMidYMid slice"'
        alertContent        = alertContent + 'focusable="false" role="img"><rect class="headline-label-color" width="100%" height="100%" fill="#28a745"></rect></svg>'
        alertContent        = alertContent + '<strong class="mr-auto headline-text"></strong>'
        alertContent        = alertContent + '<small class="text-muted">Agora</small>'
        alertContent        = alertContent + '<button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close"><span aria-hidden="true">&times;</span></button>'
        alertContent        = alertContent + '</div><div class="toast-body message-main-text"></div></div>'

        var $alertContent = $(alertContent);
        $alertContent.find('.headline-label-color').attr('fill', headlineColorLabel);
        $alertContent.find('.headline-text').text(headlineText);
        $alertContent.find('.headline-text').css('color', headlineColorLabel);
        $alertContent.find('.message-main-text').text(messageMainText);

        $('#global-dj-messages-wrapper').append($alertContent);

        Options = {
            delay: 2500,
        }

        $alertContent.toast(Options);

        $alertContent.toast('show');

        setTimeout(function() {
            $alertContent.remove();
        }, 2550);

    }
    

});