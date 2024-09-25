{
    # Module forked from https://github.com/a2systems/l10n_ar_iva_import
    "name": "l10n_ar_iva_import",
    "summary": """
        This module allows users to import all IVA data from AFIP into Odoo""",
    "author": "mariogustavoorrillo, Nahe Consulting Group",
    "maintainers": ["nahe-consulting-group"],
    "website": "https://nahe.com.ar/",
    "license": "AGPL-3",
    "category": "Accounting",
    "version": "17.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "depends": ["base", "account"],
    "data": [
        "views/account_iva_file_views.xml",
        "views/account_move_views.xml",
        "security/ir.model.access.csv",
    ],
}
