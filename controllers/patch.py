from odoo import http, fields, models
from odoo.http import request
import json

#create a patch method for material
class PatchController(http.Controller):
    @http.route('/material', auth='public', type="json", methods=['PATCH'])
    def patchMaterial(self, **kwargs):
        try:
            record = request.env['black.mesa.material'].search([('id', '=', http.request.params['id'])]).write(kwargs)
            if record:
                return json.dumps({
                    'message': 'Material updated successfully'
                })
        except Exception as e:
            return json.dumps({"error": "Missing field : " + str(e)})
