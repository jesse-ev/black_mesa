from odoo import api, fields, models


class Workspace(models.Model):
    _name = 'black.mesa.workspace'
    _description = 'Workspace'

    name = fields.Char(string='Name')

    # build_id = fields.Many2one(
    #     string='Builds',
    #     comodel_name='black.mesa.build',
    #     # required=True,
    #     readonly=True,
    # )

    build_id = fields.Integer(
        string='Build ID',
        readonly=True,
    )
    

    material_ids = fields.One2many(
        string='Materials',
        comodel_name='black.mesa.build.material.details',
        inverse_name='build_id',
        # required=True,
    )

    scientist_id = fields.Many2one(
        string='Scientist',
        comodel_name='res.partner',
        domain=[('role', '=', 'scientist')],
    )

    security_id = fields.Many2one(
        string='Security',
        comodel_name='res.partner',
        domain=[('role', '=', 'security')],
    )

    engineer_id = fields.Many2one(
        string='Engineer',
        comodel_name='res.partner',
        domain=[('role', '=', 'engineer')],
    )



