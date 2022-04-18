# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    total_qty = fields.Float('Total Quantity', digits=dp.get_precision('Product Unit of Measure'), compute="_compute_total_qty")
    print_with_barcode = fields.Boolean("Print With Barcode")
    x_quotetemplate=fields.Html('Quote Template')
    x_branch= ([('Service','Service'), ('Trading','Trading')],'Branch')
    x_subject=fields.selection([('KD','Quotation for Kitchen Exhaust Cleaning & Services'), ('WT','Quotation for Water Tank Cleaning & Disinfection'), ('DL','Quotation for Drain Line Cleaning & Block Removal'), ('GT','Quotation for Grease Trap Cleaning & Waste Disposal'), ('PST','Quotation for Pest Control Services'), ('DSF','Quotation for Disinfection & Sanitization Services'), ('QA','Quotation')],'Subject')
    def _compute_total_qty(self):
        for rec in self:
            qty = 0
            for line in rec.order_line:
                qty += line.product_uom_qty
            rec.total_qty = qty
    

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
     
    total_qty = fields.Float('Total Quantity', digits=dp.get_precision('Product Unit of Measure'), compute="_compute_total_qty")
    show_barcode = fields.Boolean("Print With Barcode")
     
    def _compute_total_qty(self):
        for rec in self:
            qty = 0
            for line in rec.order_line:
                qty += line.product_uom_qty
            rec.total_qty = qty
     
            
class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    move_total_qty = fields.Float('Total Quantity', digits=dp.get_precision('Product Unit of Measure'), compute="_compute_total_qty")
    move_line_total_qty = fields.Float('Total Qty', digits=dp.get_precision('Product Unit of Measure'), compute="_compute_total_qty")
    show_barcode = fields.Boolean("Print With Barcode")
    
    def _compute_total_qty(self):
        for rec in self:
            qty = 0
            line_qty = 0
            for line in rec.move_lines:
                qty += line.product_uom_qty
            for line in rec.move_line_ids:
                line_qty += line.qty_done
            rec.move_total_qty = qty
            rec.move_line_total_qty = line_qty
     


class AccountInvoice(models.Model):
    _inherit = 'account.move'
     
    total_qty = fields.Float('Total Quantity',digits=dp.get_precision('Product Unit of Measure'), compute="_compute_total_qty")
    show_barcode = fields.Boolean("Print With Barcode") 
    
    def _compute_total_qty(self):
        for rec in self:
            qty = 0
            for line in rec.invoice_line_ids:
                pass
                qty += line.quantity
            rec.total_qty = qty
     

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    barcode = fields.Char('Barcode', related="product_id.barcode")
    x_Frequencymonth = fields.integer('Frequency/Month')
    x_Frequencyyear = fields.integer('Frequency/ Year')
    x_location = fields.many2one('res.partner', 'Location', required=True)
    
class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    barcode = fields.Char('Barcode', related="product_id.barcode")
    
class AccountInvoiceLine(models.Model):
    _inherit = 'account.move.line'
    
    barcode = fields.Char('Barcode', related="product_id.barcode")
    
class StockMove(models.Model):
    _inherit = 'stock.move'
    
    barcode = fields.Char('Barcode', related="product_id.barcode")

                
class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    
    barcode = fields.Char('Barcode', related="product_id.barcode")
    
    
    
    
