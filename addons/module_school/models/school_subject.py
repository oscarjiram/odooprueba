from odoo import models, fields


class SchoolSubject(models.Model):
    _name = "school.subject"
    _description = "School Subject"

    name = fields.Char(
        string="Nombre",
        required=True
    )
    credits = fields.Integer(
        string="Creditos"
    )
    max_students = fields.Integer(
        string="Máximo de estudiantes"
    )
    active = fields.Boolean(
        string="Activo"
    )
    teacher_id = fields.Many2one(
        "school.teacher",
        string="Profesor"
    )
    student_ids = fields.Many2many(
        "school.student",
        string="Estudiantes"
    )
