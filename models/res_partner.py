# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    account_iva_file_id = fields.Many2one("account.iva.file", string="Archivo de IVA")
