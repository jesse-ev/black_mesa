from odoo import models, fields


class Staff(models.Model):
    _inherit = 'res.partner'

    role = fields.Selection(
        string='Role / Job', 
        selection=[
            ('scientist', 'Scientist'), 
            ('security', 'Security'),
            ('engineer', 'Engineer'),],
        required=True,
    )

    race = fields.Selection(
        string='Race', 
        selection=[
            ('human', 'Human'), 
            ('vortigaunt', 'Vortigaunt'),
            ('combine','Combine'),
            ('stalker','Stalker')],
        required=True,
    )
    
    reference = fields.Selection(
        string='Reference',
        selection=[
            ('black_mesa', 'Black Mesa'),
            ('aperture_science', 'Aperture Science'),
        ],
        required=True,
    )
    