from odoo import http, fields, models
from odoo.http import request
import json

class GetController(http.Controller):
    '''
    GET Routes
    /material - Get all materials
    /material?id='id' - Get material by id 
    /inventory - Get all inventories
    /inventory?id='id' - Get inventory by id
    /staff - Get all staff
    /staff?id='id' - Get staff by id
    /staff?role='role' - Get staff by role

    Notes for /staff:
    - role is a string
    - role can be 'scientist', 'security', 'engineer'
    - id is checked first, then role
    '''
    

    @http.route('/material', auth='public', methods=['GET'])
    def getMaterial(self, **kwargs):
        try:
            if kwargs.get('id'):
                res = request.env['black.mesa.material'].search([('id', '=', kwargs.get('id'))])
                if res:
                    return json.dumps({
                        'id': res.id,
                        'name' : res.name,
                        'qty' : res.qty,
                        'description' : res.description,
                        'source' : res.source,
                    })
                else:
                    return json.dumps({
                        'error': 'Material not found'
                    })
            else:
                return json.dumps([{
                    'id': material.id,
                    'name': material.name,
                    'qty': material.qty,
                    'description': material.description,
                    'source': material.source,
                } for material in request.env['black.mesa.material'].search([])], default=str)
        except Exception as e:
            return json.dumps({"error": str(e)})

    @http.route('/inventory', auth='public', methods=['GET'])
    def getInventory(self, **kwargs):
        try:
            if kwargs.get('id'):
                res = request.env['black.mesa.inventory'].search([('id', '=', kwargs.get('id'))])
                if res:
                    return json.dumps({
                        'id': res.id,
                        'name' : res.name,
                        'qty' : res.qty,
                        'description' : res.description,
                        'date_created' : res.date_created,
                        'image' : 'web/image?model=black.mesa.inventory&id=' + str(res.id) +'&field=image',
                    })
                else:
                    return json.dumps({
                        'error': 'Inventory not found'
                    })
            else:
                return json.dumps([{
                    'id': inventory.id,
                    'name': inventory.name,
                    'qty': inventory.qty,
                    'description': inventory.description,
                    'date_created': inventory.date_created,
                    'image': 'web/image?model=black.mesa.inventory&id=' + str(inventory.id) +'&field=image',
                } for inventory in request.env['black.mesa.inventory'].search([])], default=str)
        except Exception as e:
            return json.dumps({"error": str(e)})

    #Get staff
    @http.route('/staff', auth='public', methods=['GET'])
    def getStaff(self, **kwargs):
        try:
            if kwargs.get('role'):
                roles = ['scientist', 'security', 'engineer']
                if kwargs.get('role') in roles:
                    res = request.env['res.partner'].search([('role', '=', kwargs.get('role'))])
                    if res:
                        return json.dumps([{
                            'id': staff.id,
                            'name': staff.name,
                            'role': staff.role,
                            'race': staff.race,
                            'reference': staff.reference,
                        } for staff in res])
                    else:
                        return json.dumps({
                            'error': 'Staff not found'
                        })
                else:
                    return json.dumps({"error": "Invalid role"})
            elif kwargs.get('id'):
                res = request.env['res.partner'].search([('id', '=', kwargs.get('id'))])
                if res:
                    return json.dumps({
                        'id': res.id,
                        'name' : res.name,
                        'role' : res.role,
                        'race' : res.race,
                        'reference' : res.reference,
                    })
                else:
                    return json.dumps({
                        'error': 'Staff not found'
                    })
            else:
                return json.dumps([{
                    'id': staff.id,
                    'name': staff.name,
                    'role': staff.role,
                    'race': staff.race,
                    'reference': staff.reference,
                } for staff in request.env['res.partner'].search([])])
        except Exception as e:
            return json.dumps({"error": str(e)})
    
    #get build
    @http.route('/build', auth='public', methods=['GET'])
    def getBuild(self, **kwargs):
        try:
            if kwargs.get('id'):
                res = request.env['black.mesa.build'].search([('id', '=', kwargs.get('id'))])
                if res:
                    return json.dumps({
                        'id': res.id,
                        'name' : res.name,
                        'type' : res.type,
                        'qty' : res.qty,
                        'description' : res.description,
                        'materials' : [{
                            'id': material.id,
                            'name': material.material_id.name,
                            'qty': material.qty,
                        } for material in res.material_ids],
                        'scientist': {
                            'id': res.scientist_id.id,
                            'name': res.scientist_id.name,
                            'race': res.scientist_id.race,
                            'reference': res.scientist_id.reference,
                        },
                        'engineer': {
                            'id': res.engineer_id.id,
                            'name': res.engineer_id.name,
                            'race': res.engineer_id.race,
                            'reference': res.engineer_id.reference,
                        },
                        'security': {
                            'id': res.security_id.id,
                            'name': res.security_id.name,
                            'race': res.security_id.race,
                            'reference': res.security_id.reference,
                        },
                        'image' : 'image',
                        'state' : res.state,
                    })
                else:
                    return json.dumps({
                        'error': 'Build not found'
                    })
            else:
                return json.dumps([{
                    'id': build.id,
                    'name': build.name,
                    'type': build.type,
                    'qty': build.qty,
                    'description': build.description,
                    'materials' : [{
                        'id': material.id,
                        'name': material.material_id.name,
                        'qty': material.qty,
                    } for material in build.material_ids],
                    'scientist': {
                        'id': build.scientist_id.id,
                        'name': build.scientist_id.name,
                        'race': build.scientist_id.race,
                        'reference': build.scientist_id.reference,
                    },
                    'engineer': {
                        'id': build.engineer_id.id,
                        'name': build.engineer_id.name,
                        'race': build.engineer_id.race,
                        'reference': build.engineer_id.reference,
                    },
                    'security': {
                        'id': build.security_id.id,
                        'name': build.security_id.name,
                        'race': build.security_id.race,
                        'reference': build.security_id.reference,
                    },
                    'image': 'image',
                    'state': build.state,
                } for build in request.env['black.mesa.build'].search([])], default=str)
        except Exception as e:
            return json.dumps({"error": str(e)})