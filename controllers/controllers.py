# -*- coding: utf-8 -*-
from asyncio.log import logger
import logging
import werkzeug
import json
import base64

import odoo.http as http
from odoo.http import request
from odoo import SUPERUSER_ID
from datetime import datetime, timedelta, time
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
import odoo.http as http

logger = logging.getLogger(__name__)

class GossisteOpen(http.Controller):
    
    @http.route('/grossiste_form/', type="http", auth="public", website=True)
    def grossiste_form(self, **kw):
        print("View value...........")
        print("Grossiste from here............................")
        return http.request.render("gossiste_open.create_grossiste_form", {})
    
    @http.route('/grossiste/form/', type="http", auth="public", website=True)
    def create_grossiste(self, **post):
        # partner_brw = request.env['res.users'].sudo().browse(request._uid)
        # if len(partner_brw) > 0:
        #     logger.info("UUUUUUUUPPPPPP".format(partner_brw))
        Attachments = request.env['ir.attachment']
        if post:
            upload_file = post['images']
            upload_file1 = post['card_image']
            upload_file2 = post['card_image1']
            upload_file3 = post['card_image_sign']
            name_manager = post['name_manager']
            sub_manager = post['sub_manager']
            partner_id = post['partner_id']
            gender = post['gender']
            phone = post['phone']
            work = post['work']
            address = post['work']
            city = post['city']
            gps = post['gps']
            contact_manager = post['contact_manager']
            sub_num = post['sub_num']
            card = post['card']
            boutiquePrincipale = post['boutiquePrincipale']
            nameBAbidjan = post['nameBAbidjan']
            nameBItern = post['nameBItern']
            nb_boutique = post['nb_boutique']
            nb_vendu = post['nb_vendu']
            
            vals = {
                    'partner_id': partner_id,
                    'name_manager': name_manager,
                    'sub_manager': sub_manager,
                    'gender': gender,
                    'phone': phone,
                    'work': work,
                    'address' : address,
                    'city': city,
                    'gps' : gps,
                    'contact_manager' : contact_manager,
                    'sub_num' : sub_num,
                    'card' : card,
                    'boutiquePrincipale' : boutiquePrincipale,
                    'nameBAbidjan' : nameBAbidjan,
                    'nameBItern' : nameBItern,
                    'nb_boutique' : nb_boutique,
                    'nb_vendu' : nb_vendu,
                    }
            grossiste_obj = request.env['form.grossiste'].sudo().create(vals)
            if upload_file:
                attachment_id = Attachments.sudo().create({
                    'name': upload_file.filename,
                    'type': 'binary',
                    'datas': base64.encodestring(upload_file.read()),
                    'name': upload_file.filename,
                    'public': True,
                    'res_model': 'ir.ui.view',
                    'res_id': False,
                    'grossiste_obj_id' : grossiste_obj.id,
                })
            if upload_file1:
                attachment_id = Attachments.sudo().create({
                    'name': upload_file1.filename,
                    'type': 'binary',
                    'datas': base64.encodestring(upload_file1.read()),
                    'name': upload_file.filename,
                    'public': True,
                    'res_model': 'ir.ui.view',
                    'res_id': False,
                    'grossiste_obj_id' : grossiste_obj.id,
                })
            if upload_file2:
                attachment_id = Attachments.sudo().create({
                    'name': upload_file2.filename,
                    'type': 'binary',
                    'datas': base64.encodestring(upload_file2.read()),
                    'name': upload_file.filename,
                    'public': True,
                    'res_model': 'ir.ui.view',
                    'res_id': False,
                    'grossiste_obj_id' : grossiste_obj.id,
                })
            if upload_file3:
                attachment_id = Attachments.sudo().create({
                    'name': upload_file3.filename,
                    'type': 'binary',
                    'datas': base64.encodestring(upload_file3.read()),
                    'name': upload_file.filename,
                    'public': True,
                    'res_model': 'ir.ui.view',
                    'res_id': False,
                    'grossiste_obj_id' : grossiste_obj.id,
                })
                
                if len(attachment_id) > 0:
                    logger.info("YYYYYYY------OOOOOO-------{}--PPPP".format(attachment_id))
        return request.render("gossiste_form.grossiste_thank", {})
        # partner = kw.get('name', False)
        # logger.info("-----------DDDDDDDDD--------", partner)
        
        # image = kw.get('images', False)
        # image1 = kw.get('card_image', False)
        # image2 = kw.get('card_image1', False)
        # image3 = kw.get('card_image_sign', False)
        # kw.update({
        #     ''
        #     'name': partner,
        #     'images': base64.encodestring(image.read()) if image else False,
        #     # 'card_image': base64.encodestring(image1.read()) if image1 else False,
        #     # 'card_image1': base64.encodestring(image2.read()) if image2 else False,
        #     # 'card_image_sign': base64.encodestring(image3.read()) if image3 else False
        # })
        # print("Data request...........", kw)
        # en = request.env['form.grossiste'].sudo().create(kw)
        # logger.info("jscusbcusbcubscubcubdc", en)     
        
    
    
    # @http.route('/grossiste/form/', type='http', auth="public", website=True)
    # def upload_files(self, **post):
    #     values = {}
    #     if post.get('images',False):
    #         Attachments = request.env['ir.attachment']
    #         name = post.get('images').filename      
    #         file = post.get('images')
    #         images = file.read() 
    #         attachment_id = Attachments.sudo().create({
    #             'name': name,
    #             'type': 'binary',   
    #             'res_model': 'ir.ui.view',
    #             'res_id': False,
    #             'datas': images.encode('base64'),
    #             'public': True,
    #         })
    #         value = {
    #             'images' : attachment_id
    #         }
            
    #     return request.render("gossiste_form.grossiste_thank", value)
    
    # @http.route('/gossiste_open/gossiste_open/objects/', auth='public')
    # def list(self, **kw):
    #     return http.request.render('gossiste_open.listing', {
    #         'root': '/gossiste_open/gossiste_open',
    #         'objects': http.request.env['gossiste_open.gossiste_open'].search([]),
    #     })

    # @http.route('/gossiste_open/gossiste_open/objects/<model("gossiste_open.gossiste_open"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('gossiste_open.object', {
    #         'object': obj
    #     })
        
# class GrossisteForm(CustomerPortal):

#     @http.route('/grossiste_form', type="http", auth="public", website=True)
#     def submit_grossiste_form(self, **kw):
#         """Let's public and registered user submit a support ticket"""
#         name = ""
#         if http.request.env.user.name != "Public user":
#             name = http.request.env.user.name
        
#         customer = http.request.env.user.partner_id.name
#         email = http.request.env.user.partner_id.email
#         phone = http.request.env.user.partner_id.phone
#         values = {'partner_id' : customer,'user_ids': name,'email':email,'phone':phone}
        
#         return http.request.render('grossiste_form.submit_grossiste_form', values)
    
    
#     @http.route('/grossiste_form/thanks', type="http", auth="public", website=True)
#     def support_grossiste_thanks(self, **post):
#         """Displays a thank you page after the user submits a support ticket"""
#         if post.get('debug'):
#             return request.render("grossiste_form.support_thank_you")