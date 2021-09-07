$(document).ready(function() {
    setupNavigation();
});

function setupNavigation() {

    const navigation = $('aside#navigation');
    const currentModuleId = navigation.data('current-module-id');
    const currentModule = navigation.find('li[data-module-id=' + currentModuleId + ']');

    activeModule(currentModule);
    onClickItemModule();

    function onClickItemModule() {
        navigation.find('li.list-group-item-module').click(function(event) {
            event.preventDefault();
            const clickedModule = $(this);
            const clickedModuleActive = clickedModule.data('module-active');
            if (clickedModule.data('module-active')) {
                deactivateModule(clickedModule);
            } else {
                activeModule(clickedModule);
            };
        });
    };

    function activeModule(module) {
        console.log(navigation.find('.list-group-item-module-active').parent('li').length);
        module.addClass('list-group-item-module-active');
        module.data('module-active', true);
        openModule(module);
    };

    function deactivateModule(module) {
        module.removeClass('list-group-item-module-active');
        module.data('module-active', false);
        closeModule(module);
    };

    function openModule(module) {
        module.find('.list-group.navigation-sub').removeClass('d-none');
        module.find('i.closed').addClass('d-none');
        module.find('i.open').removeClass('d-none');
    };

    function closeModule(module) {
        module.find('.list-group.navigation-sub').addClass('d-none');
        module.find('i.closed').removeClass('d-none');
        module.find('i.open').addClass('d-none');
    };

    //document.location = $(this).data('url');

};
