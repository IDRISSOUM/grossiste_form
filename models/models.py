# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gossiste_open(models.Model):
#     _name = 'gossiste_open.gossiste_open'
#     _description = 'gossiste_open.gossiste_open'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
