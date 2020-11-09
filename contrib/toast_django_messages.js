(function (factory, jQuery, Zepto) {

    if (typeof define === 'function' && define.amd) {
        define(['jquery'], factory);
    } else if (typeof exports === 'object') {
        module.exports = factory(require('jquery'));
    } else {
        factory(jQuery || Zepto);
    }

} (function ($) {

$.fn.djangoMessages = function(message, type, time) {



}

}, window.jQuery, window.Zepto));