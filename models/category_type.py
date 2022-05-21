# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval

import logging
_logger = logging.getLogger(__name__)

class GossisteOpenCategoryType(models.Model):
    _name='marchand.category'
    _description = "Grossiste Category Type"

    name = fields.Char('Type de Marchand')