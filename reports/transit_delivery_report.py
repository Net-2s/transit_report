# -*- coding: utf-8 -*-

from odoo import api, models


class TransitDeliveryReport(models.AbstractModel):
    _name = 'report.transit.delivery.report'
    _description = 'Transit Delivery Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['stock.picking'].browse(docids)
        return {
            'doc_ids': docs.ids,
            'doc_model': 'stock.picking',
            'docs': docs,
        }
