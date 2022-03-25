from odoo import api, fields, models


class Inventory(models.Model):
    _name = 'black.mesa.inventory'
    _description = 'Inventory'

    name = fields.Char(string='Name')
    
    qty = fields.Integer(string='Quantity')

    description = fields.Text(string='Description')

    date_created = fields.Datetime(string='Date Created')

    image = fields.Binary(string='Image')
