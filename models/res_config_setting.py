# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval

import logging
_logger = logging.getLogger(__name__)

class GrossisteOpenResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"
    
    grossiste_form_visible = fields.Selection([
        ('public_user_grossiste', 'Grossiste From For All Public User'),
        ('login_user_grossiste', 'Grossiste From For Login User'),
    ], string='Grossiste Form',default='public_user_grossiste')

    support_team_id = fields.Many2one('support.team', string = "Default Support Team")
    
    def get_values(self):
        res = super(GrossisteOpenResConfigSettings, self).get_values()
        team_id = self.env['ir.config_parameter'].sudo().get_param('grossiste_form.support_team_id')
        res.update(
            grossiste_from_visible = self.env['ir.config_parameter'].sudo().get_param('grossiste_form.grossiste_form_visible'),
            support_team_id = int(team_id) or False,
        )
        return res

    def set_values(self):
        super(GrossisteOpenResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('grossiste_form.grossiste_from_visible', self.grossiste_from_visible)
        self.env['ir.config_parameter'].sudo().set_param('grossiste_form.support_team_id', self.support_team_id.id)
        