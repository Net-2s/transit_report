# -*- coding: utf-8 -*-

from odoo import models
from odoo.tools.image import image_data_uri
import base64


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    _description = 'stock.picking'
