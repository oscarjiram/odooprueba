from odoo import models, fields, api
from datetime import date


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(
        string="Nombre",
        required=True
    )
    birth_date = fields.Date(
        string="Cumpleaños"
    )
    age = fields.Integer(
        string="Edad",
        compute="_compute_age",
        store=True
    )
    final_exam_grade = fields.Float(
        string="Nota"
    )
    subjects_ids = fields.Many2many(
        "school.subject",
        string="Aula"
    )

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
