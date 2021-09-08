$(document).ready(function() {
    setupNavigation();
});

function setupNavigation() {

    const navigation = $('aside#navigation');

    module();
    submodule();

    function module() {
        const currentModule = navigation.find('li[data-module-id=' + navigation.data('current-module-id') + ']');
        console.log('li[data-module-id=' + navigation.data('current-module-id') + ']');
        activeModule(currentModule);
        navigation.find('li.list-group-item-module').click(function(event) {
            event.preventDefault();
            const clickedModule = $(this);
            const clickedModuleActive = clickedModule.data('module-active');
            if (clickedModuleActive) {
                deactivateModule(clickedModule);
            } else {
                activeModule(clickedModule);
            };
        });
    };

    function activeModule(module) {
        navigation.find('.list-group-item-module-active').each(function() {
            deactivateModule($(this));
        });
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

    function submodule() {
        const currentSubmodule = navigation.find('li[data-submodule-id=' + navigation.data('current-submodule-id') + ']');
        activeSubmodule(currentSubmodule);
        navigation.find('.list-group-item-submodule').click(function(e) {
            e.preventDefault();
            document.location = $(this).data('url');
        });
    };

    function activeSubmodule(submodule) {
        submodule.find('.list-group-item-submodule-content').addClass('active');
    };

};
