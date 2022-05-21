odoo.define('grossiste_open.grossiste_open', function (require) {
    'use strict';
        require('web.dom_ready');
        var core = require('web.core');
        var ajax = require('web.ajax');
        var rpc = require('web.rpc');
        var request
        var _t = core._t;
        $(document).ready(function(){
            var priority_value = $('#priority_value').val()
            $('#grossiste').val(priority_value)
        });
    });