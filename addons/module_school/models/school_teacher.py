from odoo import models, fields


class Schoolteacher(models.Model):
    _name = "school.teacher"
    _description = "School Teacher"

    name = fields.Char(
        string="Nombre",
        required=True
    )
    profile = fields.Text(
        string="Perfil"
    )
    subjects_ids = fields.One2many(
        "school.subject",
        "teacher_id",
        string="Aula"
    )


