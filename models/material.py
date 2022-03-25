from odoo import api, fields, models


class Material(models.Model):
    _name = 'black.mesa.material'
    _description = 'Material'

    name = fields.Char(string='Name', required=True)
    qty = fields.Integer(string='Quantity', required=True)
    description = fields.Text(string='Description')
    
    source = fields.Selection(
        string='Source of Material',
        selection=[('earth', 'Earth'), ('xen', 'Xen')],
        required=True
    )

    image = fields.Binary(string='Image')
    
    

