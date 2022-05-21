# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval

import logging
_logger = logging.getLogger(__name__)

class GrossisteOpenWebsite(models.Model):

    _inherit = "website"
    
    def get_grossiste_details(self):
        partner_brw = self.env['res.users'].browse(self._uid)
        grossiste_ids = self.env['form.grossiste'].sudo().search(['|',('partner_id','=',partner_brw.partner_id.id),('user_id','=',partner_brw.id)])
        return grossiste_ids
    
    # def get_partner_list(self):
    #     partner_team_ids=self.env['res.partner'].sudo().search([])
    #     return partner_team_ids

    def get_partner_list(self):
        partner_id = self.env['res.users'].sudo().search([])
        _partner = []
        for partner in partner_id :
            _partner.append(partner)
        return _partner
    
class GrossisteOpenIrAttachment(models.Model):
    _inherit='ir.attachment'
    
    grossiste_obj_id = fields.Many2one('form.grossiste', 'Form Grossiste')



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
