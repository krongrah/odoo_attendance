from odoo import models, fields

class Employee(models.Model):
    _name = 'employee'

    realName = fields.Char(required=True, string="name")
    checkedIn = fields.Boolean()
    perm_read = fields.Boolean(string='Read Access')