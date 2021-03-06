from odoo import api, fields, models
from odoo.exceptions import ValidationError
import string
import random


class Build(models.Model):
    _name = 'black.mesa.build'
    _description = 'Black mesa build'

    name = fields.Char(
        string='Name',
        required=True,
    )

    type = fields.Selection(
        string='Type',
        selection=[
            ('weapon', 'Weapon'),
            ('teleporter', 'Teleporter'),
            ('vehicle', 'Vehicle'),
        ],
        required=True,
    )

    qty = fields.Integer(
        string='Quantity',
        required=True,
    )

    description = fields.Text(string='Description')

    material_ids = fields.One2many(
        string='Materials',
        comodel_name='black.mesa.build.material.details',
        inverse_name='build_id',
        required=True,
    )

    scientist_id = fields.Many2one(
        string='Scientist',
        comodel_name='res.partner',
        domain=[('role', '=', 'scientist')],
        required=True,
    )

    security_id = fields.Many2one(
        string='Security',
        comodel_name='res.partner',
        domain=[('role', '=', 'security')],
        required=True,
    )

    engineer_id = fields.Many2one(
        string='Engineer',
        comodel_name='res.partner',
        domain=[('role', '=', 'engineer')],
        required=True,
    )

    image = fields.Binary(string='Image', default=False)

    state = fields.Selection(
        string='State',
        selection=[
            ('manufacture', 'Manufacture'),
            ('queue', 'Queued'),
            ('finished', 'Finished'),
            ('canceled', 'Canceled'),
        ],
        default='manufacture',
        required=True,
        readonly=True,
    )

    @api.model
    def create(self, vals):
        vals['state'] = 'queue'
        return super(Build, self).create(vals)

    def unlink(self):
        if self.state == 'canceled':
            for obj in self:
                for item in self.material_ids:
                    item.unlink()

        return super(Build, self).unlink()

    @api.constrains('qty')
    def _check_qty(self):
        if self.qty < 0:
            raise ValidationError('Quantity must be positive')


    '''Button Methods'''
    def create_inv(self):
        self.state = 'finished'
        new_inv = self.env['black.mesa.inventory'].create({
            'name': self.name,
            'qty': self.qty,
            'description': self.description,
            'date_created': fields.Datetime.now(),
            'image': self.image,
        })

        product = self.env['product.template'].create({
            'name': self.name,
            'sale_ok': True,
            'purchase_ok': True,
            'type': 'consu',
            'categ_id': 1, #1 means All category 
            'list_price': 0,
            'description_sale': self.description,
            'description_purchase': self.description,
            'description': self.description,
            'image_1920': self.image,
            'default_code': "BM_PROD_" + str(self.name),
            'barcode': "BM_PROD_" + str(self.name) + "_" + str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))),
        })

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Build successful!',
                'type': 'rainbow_man',
            }
        }

    def button_see_inventory(self):
        return {
            'res_model' : 'black.mesa.inventory',
            'type' : 'ir.actions.act_window',
            'view_mode' : 'form',
            'view_type' : 'form',
            'res_id' : self.env['black.mesa.inventory'].search([('name', '=', self.name)]).id,
            'target' : 'self',
        }
    
    def cancel(self):
        self.state = 'canceled'
        return True

    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Build name must be unique!'),
    ]


class BuildMaterialDetails(models.Model):
    _name = 'black.mesa.build.material.details'
    _description = 'Black mesa build material details'

    build_id = fields.Many2one(
        string='Build',
        comodel_name='black.mesa.build',
    )

    material_id = fields.Many2one(
        string='Material',
        comodel_name='black.mesa.material',
        required=True,
    )

    qty = fields.Integer(
        string='Quantity',
        required=True,
    )

    @api.constrains('qty')
    def _check_qty(self):
        for record in self:
            available_stock = self.env['black.mesa.material'].search([('id', '=', record.material_id.id), ('qty', '<', record.qty)])
            if len(available_stock) > 0:
                raise ValidationError('Not enough materials!')

    @api.model
    def create(self,vals):
        record = super(BuildMaterialDetails, self).create(vals) 
        if record.qty:
            self.env['black.mesa.material'].search([('id','=',record.material_id.id)]).write({'qty':record.material_id.qty - record.qty})
            return record
    
    def unlink(self):
        if self.env['black.mesa.build'].search([('id','=',self.build_id.id)]).state == 'canceled':
            self.env['black.mesa.material'].search([('id','=',self.material_id.id)]).write({'qty':self.material_id.qty + self.qty})
            # for obj in self:
            #     self.env['black.mesa.material'].search([('id','=',obj.material_id.id)]).write({'qty':obj.material_id.qty + obj.qty})
        record = super(BuildMaterialDetails, self).unlink()