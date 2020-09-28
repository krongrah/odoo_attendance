from odoo import models, fields

class Attendance(models.Model):
    _name = 'attendance'
    checkin = fields.Datetime(required=True)
    checkout = fields.Datetime()
