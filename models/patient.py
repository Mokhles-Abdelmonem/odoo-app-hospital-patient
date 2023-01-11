from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date



class Hospital_patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'

    name = fields.Char(string="Name", required=True, tracking=True)
    ref = fields.Char(string="Refrence")
    age = fields.Integer(string="Age",compute="compute_age", tracking=True)
    is_child = fields.Boolean(string="Is Child ?", tracking=True)
    notes = fields.Text(string="Notes", tracking=True)
    active = fields.Boolean(string="Active", default=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
                              string="Gender", tracking=True)
    date_of_birth = fields.Date(string="birthday")
    appointment_id = fields.Many2one('hospital.appointment', string="Appointments")


    @api.constrains('age', 'is_child')
    def check_child_age(self):
        if self.age <= 0 :
            raise ValidationError(_("Age has to at least one !"))
        if self.age <= 10 and not self.is_child :
            raise ValidationError(_("Age at 10 or  less is child !"))
        if self.is_child and self.age > 10 :
            raise ValidationError(_("Age more than 10 is not a child !"))


    @api.depends('date_of_birth')
    def compute_age(self):
        for rec in self:
            this_year = date.today().year
            rec.age = this_year - rec.date_of_birth.year if rec.date_of_birth else 1


    @api.onchange('age')
    def onchange_age(self):
        self.is_child = True if self.age <= 10 else False

