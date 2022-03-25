from odoo import http, fields, models
from odoo.http import request
import json

#write post method for material
class PostController(http.Controller):

    '''
    POST Routes
    /material - Create a new material
    fields:
        name - string
        qty - integer
        description - text
        source - earth or xen
    '''

    @http.route('/material', auth='public', type="json", methods=['POST'])
    def postMaterial(self, **kwargs):
        try:
            name = http.request.params['name']
            qty = http.request.params['qty'] 
            description = http.request.params['description'] 
            source = http.request.params['source']
            if name and qty and source:
                request.env['black.mesa.material'].create({
                    'name': name,
                    'qty': qty,
                    'description': description,
                    'source': source,
                })
                return json.dumps({
                    'message': 'Material created successfully'
                })
            else:
                message = 'Missing required fields : '
                if not name:
                    message += 'name, '
                if not qty:
                    message += 'qty, '
                if not source:
                    message += 'source, '
                return json.dumps({
                    'error': 'Missing required fields'
                })
        except Exception as e:
            return json.dumps({"error": "Missing field : " + str(e)})
