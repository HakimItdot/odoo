# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ListPricePercent(models.Model):
    _inherit = 'product.template'

    
    percent_margin = fields.Float(
        string='Marge %',
        track_visibility='always',
        readonly=False,
        size=10,
        required=True
    )
    
    @api.onchange('standard_price', 'percent_margin')
    def _compute_list_price(self):
        Coeff = 1.9/1.0983
        for record in self:
            if record.percent_margin:
                record.list_price = 0
                new_pm = Coeff * record.percent_margin
                record.list_price = record.standard_price * (1 + new_pm/100)         
                
    @api.onchange('standard_price', 'list_price')          
    def _compute_margin_price(self):
        Coeff = 1.9/1.0983
        for record in self:
            if record.list_price:
                record.percent_margin = 0
                #new_sp = Coeff * record.standard_price
                try:
                    record.percent_margin = 100*(record.list_price - record.standard_price)/(Coeff * record.standard_price)
                    #record.percent_margin = 100*(record.list_price/record.standard_price - 1)/Coeff 
                except:
                    pass
