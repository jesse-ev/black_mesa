from odoo import api, fields, models
import string
import random

class Inventory(models.Model):
    _name = 'black.mesa.inventory'
    _description = 'Inventory'

    name = fields.Char(string='Name')
    
    qty = fields.Integer(string='Quantity')

    description = fields.Text(string='Description')

    date_created = fields.Datetime(string='Date Created')

    image = fields.Binary(string='Image')

    def write(self, vals):
        self.env['product.template'].search(['default_code', '=', "BM_PROD_" + str(self.name)]).write({
            'name': vals['name'],
            'description': vals['description'],
            'description_sale': vals['description'],
            'description_purchase': vals['description'],
            'image_1920': vals['image'],
            'default_code': "BM_PROD_" + vals['name'],
            'barcode': "BM_PROD_" + vals['name'] + "_" + str(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))),
        })
        return super(Inventory, self).write(vals)
    
    def unlink(self):
        self.env['product.template'].search([('default_code', '=', "BM_PROD_" + str(self.name))]).unlink()
        return super(Inventory, self).unlink()

    def button_see_product(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'form',
            'res_id': self.env['product.template'].search([('default_code', '=', "BM_PROD_" + str(self.name))]).id,
            'target': 'current',
        }
    
    def button_create_invoice(self):
        #TODO : Actually delete the product qty from the inventory
        self.env['account.move'].create({
            'move_type': 'out_invoice',
            'invoice_line_ids': [(0, 0, {
                'product_id': self.env['product.template'].search([('default_code', '=', "BM_PROD_" + str(self.name))]).id,
                'quantity': 0,
                'price_unit': 0,
            })],
        })

        return {
            'effect': {
                'fadeout': 'fast',
                'message': 'Invoice created successfully!',
                'type': 'rainbow_man',
            }
        }

        # return {
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'account.move',
        #     'view_mode': 'form',
        #     'target': 'current',
        #     'context': {
        #         'default_move_type': 'out_invoice',
        #         'default_invoice_line_ids': [(0, 0, {
        #             'product_id': 29,
        #             'quantity': self.qty,
        #             'price_unit': 0,
        #         })],
        #     }
        # }
