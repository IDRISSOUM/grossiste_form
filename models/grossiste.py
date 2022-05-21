from email.policy import default
import string
from odoo import models, fields, api, _
import logging
from datetime import timedelta

logger = logging.getLogger(__name__)

class FormGrossite(models.Model):
    _name = 'form.grossiste'
    _description = "Form Grossiste" 
    _inherit = ['mail.thread', 'mail.thread', 'utm.mixin', 'rating.mixin', 'mail.activity.mixin']
    
    
    
    partner_id = fields.Many2one('res.users', string="E-mail commercial")
    name_manager = fields.Char(string="Nom du Responsable")
    sub_num = fields.Char(string="Téléphone gérant")
    sub_manager = fields.Char(string="Nom du gérant de la boutique")
    boutiquePrincipale = fields.Char(string="Nom de la boutique principale")
    gender = fields.Selection([('m', 'Homme'), ('f', 'Femme')], default="m", string="Genre")
    work = fields.Selection([('d', 'Distributeur'), ('g', 'Grossiste'), ('v', 'Revendeur'), ('a', 'Autre')], default="d", string="Catégorie")
    address = fields.Text(string="Adresse")
    gps = fields.Text(string="Position")
    phone = fields.Char(string="Téléphone responsable")
    nameBAbidjan = fields.Char(string="Nom des boutiques abidjan")
    nameBItern = fields.Char(string="Nom des boutiques a l’intérieur")
    nb_boutique = fields.Integer(string="Nombre de Boutique")
    nb_vendu = fields.Integer(string="Nombre de pièces vendus par mois")
    city = fields.Char(string="Ville")
    contact_manager = fields.Char(string="E-mail du responsable")
    card = fields.Char(string="CNI")
    images = fields.Image(string="Photo de la Boutique", max_width=100, max_height=100, verify_resolution=False, attachment=True, store=True)
    card_image = fields.Image(string="Photo de la Carte d\'identité recto", max_width=100, max_height=100, verify_resolution=False, attachment=True, store=True)
    card_image1 = fields.Image(string="Photo de la Carte d\'identité verso", max_width=100, max_height=100, verify_resolution=False, attachment=True, store=True)
    card_image_sign = fields.Image(string="Photo de la signature", max_width=100, max_height=100, verify_resolution=False, attachment=True, store=True)
    choice_about = fields.Boolean(string="Oui/Non")
    

    @api.model
    def create(self, vals):
        res = super(FormGrossite, self).create(vals)
        if(res):   
            logger.info("les valeurs de l'enregistrement: {} et {} ".format(vals, res))
        return res
    
    def _get_attachment_count(self):
        for ticket in self:
            attachment_ids = self.env['ir.attachment'].search([('grossiste_obj_id','=',ticket.id)])
            ticket.attachment_count = len(attachment_ids)