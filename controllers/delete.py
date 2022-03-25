from odoo import http, fields, models
from odoo.http import request
import json

#write a delete method for material
class DeleteController(http.Controller):
    
        '''
        DELETE Routes
        /material - Delete a material
        fields:
            id - integer
        '''
    
        @http.route('/material', auth='public', type="json", methods=['DELETE'])
        def deleteMaterial(self, **kwargs):
            try:
                id = http.request.params['id']
                if id:
                    request.env['black.mesa.material'].search([('id', '=', id)]).unlink()
                    return json.dumps({
                        'message': 'Material deleted successfully'
                    })
                else:
                    return json.dumps({
                        'error': 'Missing required field'
                    })
            except Exception as e:
                return json.dumps({"error": "Missing field : " + str(e)})