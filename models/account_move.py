# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    account_iva_file_id = fields.Many2one("account.iva.file", string="Archivo de IVA")
    file_amount = fields.Float("Monto Archivo IVA")
